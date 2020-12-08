from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from persistence.dao.contact_register import clients_all, contact_information_all, find_client_by_id, delete_client_and_contact, save_client
from datetime import datetime
from django.db import IntegrityError
from django.db.models import F
from energy_home.custom.library.factory.model_factory import create_client, create_contact_information, create_client_id

def inicio(request):

    return render(request, "inicio.html")

def productos(request):

    return render(request, 'productos.html')

def contacto(request):

    return render(request, 'contacto.html', {'msg_success_contact' : '', 'msg_error_contact' : ''})
    
def servicios(request):

    return render(request, 'servicios.html')

def nosotros(request):

    return render(request, 'nosotros.html')

def subjects(request):
    return render(request, "subjects.html", {'clients' : clients_all(), 'contact_informations' : contact_information_all(), 'message_delete_error': ''})        

@csrf_protect
def save_contact_info(request):

    print('save_contact_info')
    msg_success_contact = ''
    msg_error_contact = ''

    try:
        client = create_client(request)
        msg_success_contact = save_client(client, request)
        #contact_information = create_contact_information(request)
        #contact_information.attached = request.FILES.get("adjunto")
        #msg_success_contact = save_client_and_contact_info(client, contact_information)
    except Exception as e:
        print('Error:\n{0}'.format(e))
        msg_error_contact = e
    return render(request, 'contact.html', {'msg_success_contact' : msg_success_contact, 'msg_error_contact' : msg_error_contact})

   