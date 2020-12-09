from rest_framework import serializers


class ClientSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rut = serializers.CharField(required=True, max_length=18)
    nombre = serializers.CharField(required=True, max_length=350)
    direccion = serializers.CharField(required=True, max_length=150)
    email = serializers.CharField(required=True, max_length=80)
    telefono = serializers.CharField(required=True, max_length=15)

class IdSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
