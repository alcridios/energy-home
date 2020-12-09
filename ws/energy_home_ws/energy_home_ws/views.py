from django.http import JsonResponse
from persistence.dao.contact_register import client_all, contact_information_all, find_client_by_id, find_contact_information_by_client_id, find_contact_by_id, save_client
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from energy_home_ws.lib.serializers import ClientSerializers, IdSerializer
from persistence.models import Client, ContactInformation
from datetime import datetime
from django.core.files.base import ContentFile
import base64

@api_view(['GET'])
def client(request):

    if 'nombre' in request.GET:
        clients = client_all().values().filter(nombre=request.GET['nombre'])
        return JsonResponse(list(clients), safe=False)
    if 'rut' in request.GET:
        clients = client_all().values().filter(rut=request.GET['rut'])
        return JsonResponse(list(clients), safe=False)
    if 'direccion' in request.GET:
        clients = client_all().values().filter(direccion=request.GET['direccion'])
        return JsonResponse(list(clients), safe=False)
    return JsonResponse(list(client_all().values()), safe=False)

@api_view(['GET'])
def client_by_id(request, id):
    client = find_client_by_id(id)
    if client == {}:
        return JsonResponse(client, safe=False)
    else:
        return JsonResponse(model_to_dict(client))

@api_view(['GET'])
def contact_information(request):
    if 'id' in request.GET:
        contact = contact_information_all().values().filter(id=request.GET['id'])
        return JsonResponse(list(contact), safe=False)
    if 'mensaje' in request.GET:
        contact = contact_information_all().values().filter(mensaje=request.GET['mensaje'])
        return JsonResponse(list(contact), safe=False)
    if 'client' in request.GET:
        contact = contact_information_all().values().filter(client=request.GET['client'])
        return JsonResponse(list(contact), safe=False)
    return JsonResponse(list(contact_information_all().values()), safe=False)              

@api_view(['GET'])
def contact_information_by_id(request, id):
    contact = find_contact_by_id(id)
    if contact == {}:
         return JsonResponse(contact, safe=False)
    else:
        return JsonResponse(model_to_dict(contact, fields=['id','mensaje', 'image_url', 'register', 'client']))

@api_view(['POST'])
def add_client(request):
    #print('request.data -> {0}'.format(request.data))
    serializer = ClientSerializers(data=request.data)
    if serializer.is_valid():
        #CREAR CLIENT MODEL
        client=Client.json_deserializer(serializer)
        #OBTENER CONTACT INFORMATION DESDE REQUEST
        mensaje = request.data.get('mensaje')
        image_name = request.data.get('image_name')
        image_base64 = request.data.get('image')
        #print(image_base64)
        #DECODE IMAGE BASE 64
        image_decode = base64.b64decode(image_base64.replace('\n', ''))
        #IMAGE FILE
        image_field = ContentFile(image_decode, image_name)
        contact_information = ContactInformation(
            mensaje=mensaje,
            register=datetime.now(),
            attached=image_field
        )
        
        print('client -> {0}'.format(client))
        response = save_client(client, contact_information)
    return JsonResponse(response, safe=False)

@api_view(['DELETE'])
def delete_client(request):
    serializer = IdSerializer(data=request.data)

    if serializer.is_valid():
        id = serializer.data.get("id")
        print('id: {0}'.format(serializer.data.get("id")))

        client = find_client_by_id(id)
        if client == {}:
            response = {
                    'timestamp': datetime.now(),
                    'code': 1,
                    'message': 'CLIENTE NO EXISTE. ERROR AL BORRAR'}
            return JsonResponse(response, safe=False)
        else:

            contacts = ContactInformation.objects.filter(client=client.id)
            for contact in contacts:
                contact.delete()

            client.delete()
            response = {
                    'timestamp': datetime.now(),
                    'code': 0,
                    'message': 'CLIENTE BORRADO DEL SISTEMA'}
            return JsonResponse(response, safe=False)            
    else :
    
        response = {
                'timestamp': datetime.now(),
                'code': -1,
                'message': 'ERROR JSON NO VALIDO'}
        return JsonResponse(response, safe=False)


