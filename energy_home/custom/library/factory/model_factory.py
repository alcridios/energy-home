from energy_home.custom.library.validate.empty import is_emptys
from persistence.models import Client, ContactInformation
from datetime import datetime

def post_parameter(request, nombre):

    value = ''
    try:
        value = request.POST[nombre]
        print('{0}: {1}'.format(nombre, value))
    except Exception as e:
        print(e)

    return value

def get_parameter(request, nombre):

    value = ''
    try:
        value = request.GET[nombre]
        print('{0}: {1}'.format(nombre, value))
    except Exception as e:
        print(e)

    return value

def create_client(request):
    print('create_client')
    rut = post_parameter(request, 'rut')
    nombre = post_parameter(request, 'nombre')
    direccion = post_parameter(request, 'comuna')
    email = post_parameter(request, 'email')
    telefono = post_parameter(request, 'telefono')
    
    message_error = is_emptys(
        rut=rut,
        nombre=nombre,
        direccion=direccion,
        email=email,
        telefono=telefono
    )

    print('message_error: {0}'.format(message_error))

    if message_error == '':
        return Client(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            email=email,
            phone=telefono
        )
    else:
        raise Exception(message_error)

def create_contact_information(request):
    print('create_contact_information')
    mensaje = post_parameter(request, 'mensaje')
    register = datetime.now()

    message_error = is_emptys(mensaje=mensaje)
    print('message_error: {0}'.format(message_error))

    if message_error == '':
        return ContactInformation(
            mensaje=mensaje,
            register=register
        )
    else:
        raise Exception(message_error)

def create_client_id(request):
    print('create_client_id')
    id = get_parameter(request, 'id')
    message_error = is_emptys(id=id)
    if message_error == '' :
        return id
    else:
         raise Exception(message_error)
