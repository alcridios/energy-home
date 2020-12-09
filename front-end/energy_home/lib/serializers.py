from rest_framework import serializers

class ClientSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rut = serializers.CharField(required=True, max_length=18)
    nombre = serializers.CharField(required=True, max_length=350)
    direccion = serializers.CharField(required=True, max_length=150)
    email = serializers.CharField(required=True, max_length=80)
    telefono = serializers.CharField(required=True, max_length=15)

class ClientDeleteSerializers(serializers.Serializer):
    timestamp = serializers.TimeField(required=True)
    code = serializers.IntegerField(required=True)
    message = serializers.CharField(required=True, max_length=350)

class ContactInformationSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    mensaje = serializers.CharField(required=True, max_length=800)
    register = serializers.CharField(required=True)
    attached = serializers.CharField(required=True)
    client_id = serializers.IntegerField(required=True)