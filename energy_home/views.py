from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from formulario.models import datos

def inicio(request):

    return render(request, "inicio.html")

def productos(request):

    return render(request, 'productos.html')

def contacto(request):

    return render(request, 'contacto.html')
    
def servicios(request):

    return render(request, 'servicios.html')

def nosotros(request):

    return render(request, 'nosotros.html')

@csrf_protect
def save_contact_info(request):
    print('REQUEST: {0}'.format(request.POST))
    print('REQUEST: {0}'.format(request.body))

    contact = datos(
        nombre=request.POST['nombre'],
        comuna=request.POST['comuna'],
        email=request.POST['email'],
        fono=request.POST['fono'],
        mensaje=request.POST['mensaje']
    )

    contact.save()
    return render(request, 'contacto.html')

