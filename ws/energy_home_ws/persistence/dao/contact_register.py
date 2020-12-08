from persistence.models import Client, ContactInformation
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from datetime import datetime

def client_all():
    return Client.objects.all()

def contact_information_all():
    return ContactInformation.objects.all()

def find_contact_information_by_client_id(client):
    return ContactInformation.objects.get(client=client)

def find_client_by_id(id):
    try:
        return Client.objects.get(id=id)
    except Client.DoesNotExist as ex:
        print(ex)
        return {}

def find_contact_by_id(id):
    try:
        return ContactInformation.objects.get(id=id)
    except ContactInformation.DoesNotExist as ex:
        print(ex)
        return {}

def save_client(client, contact_information):
    try:
        client.save()
        print('RUT: {0}'.format(client.rut))
        message = 'CLIENTE REGISTRADO.'
        print(message)        
        contact_information.client = client
        contact_information.save()
        print('ASUNTO ALMACENADO')

    except IntegrityError as e:
        print(e)
        client.id = Client.objects.get(rut=client.rut).id
        print('CLIENTE YA SE ENCUENTRA REGISTRADO.')
        print('SE PROCEDE CON LA ACTUALIACIÓN.')
        client.save(force_update=True)
        message = 'CLIENTE ACTUALIZADO.'
        print(message)
        contact_information.client = client
       #* contact_information.save() 
        print('ASUNTO ALMACENADO')

    return {
        'timestamp': datetime.now(),
        'code': 0,
        'message': message,
        'client': client.json_serializer()
    }