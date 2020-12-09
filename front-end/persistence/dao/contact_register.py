from persistence.models import ContactInformation, Client
from energy_home.lib.serializers import ClientSerializers, ClientDeleteSerializers, ContactInformationSerializers
from django.db import IntegrityError
import requests
import json
import base64

# def save_client_and_contact_info(client, contact_information):

#     print('save_client_and_contact_info')
#     client = save_client(client)
#     contact_information.client = client
#     save_contact_information(contact_information)

#     return 'ASUNTO ALMACENADO CORRECTAMENTE.'

def save_client(client, request):

    try:
        print('contact_register-> sava_client')
        message_response = ''
        image = request.FILES.get("adjunto")
        image_base64 = base64.b64encode(image.read()).decode('utf-8')
        mensaje = request.POST.get("mensaje")

    except Exception as e:
        print(e)
        message_error_delete = 'ERROR LLAMADO SERVICIO'
        print(message_error_delete) 

    json_client = {
        'rut': client.rut,
        'nombre': client.nombre,
        'direccion': client.direccion,
        'email': client.email,
        'telefono': client.telefono,
        'image': image_base64,
        'image_name': image.name,
        'mensaje': mensaje
    }

    #print(json_client)

    

def save_contact_information(contact_information):
    print('save_contact_information')
    try:
        contact_information.save()
        print('ASUNTO ALMACENADO.')
    except IntegrityError as e:
        print(e)
    return contact_information

def clients_all():

    clients = []

    try:
        print('CALL REST SERVICE')
        response = requests.get('http://127.0.0.1:8001/api/v1/client/', timeout=(5, 15))
        for json_client in response.json():

            serializer = ClientSerializers(data=json_client)

            if serializer.is_valid():

                client = Client.json_deserializer(serializer)
                clients.append(client)
    except Exception as e:
        print(e)
        print('ERROR LLAMADO SERVICIO ') 
 

    return clients

def contact_information_all():
    contacts = []
    try:
        print('CALL REST SERVICE')
        url = 'http://127.0.0.1:8001/api/v1/contact-information/'
        response = requests.get(url)
        for json_contact in response.json ():
            serializer = ContactInformationSerializers(data=json_contact)
            if serializer.is_valid():
                contact = ContactInformation.json_deserializer(serializer)
                print(contact)
                contacts.append(contact)

    except Exception as e:
        print(e)
        print('ERROR LLAMADO SERVICIO ') 

    return contacts

def find_contact_information_by_client_id(client):
    return ContactInformation.objects.get(client=client)

def find_client_by_id(id):
    return Client.objects.get(id=id)

def delete_client_and_contact(id):
    message_error_delete = ''

    json_id = {'id': id}

    try:
        print('CALL DELETE REST SERVICE')
        response = requests.delete('http://127.0.0.1:8001/api/v1/del-client', data=json_id)
        print('response.status_code: {0}'.format(response.status_code))
        print(response.json())
        serializer = ClientDeleteSerializers(data=response.json())

        if serializer.is_valid():

            message_error_delete = serializer.data.get('message')
            
    except Exception as e:
        print(e)
        message_error_delete = 'ERROR LLAMADO SERVICIO'
        print(message_error_delete) 
    return message_error_delete
