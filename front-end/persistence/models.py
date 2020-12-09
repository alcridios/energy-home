from django.db import models


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rut = models.CharField(db_column='RUT', unique=True, max_length=18)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return 'ID: {0} | RUT: {1} -> NOMBRE: {2} {3} {4}'.format(self.id, self.rut, self.nombre, self.direccion, self.telefono)

    class Meta:
        managed = False
        db_table = 'client'

    @staticmethod
    def json_deserializer(serializer):
        return Client(
                    id=serializer.data.get('id'),
                    rut=serializer.data.get('rut'),
                    nombre=serializer.data.get('nombre'),
                    direccion=serializer.data.get('direccion'),
                    email=serializer.data.get('email'),
                    telefono=serializer.data.get('telefono'))          


class ContactInformation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mensaje = models.CharField(db_column='MENSAJE', max_length=800, blank=True, null=True)  # Field name made lowercase.
    register = models.DateTimeField(db_column='REGISTER', blank=True, null=True)  # Field name made lowercase.
    attached = models.CharField(db_column='ATTACHED', max_length=1024, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_ID', blank=True, null=True)  # Field name made lowercase.

    @staticmethod
    def json_deserializer(serializer):
        attached='http://localhost:8001/media/{0}'.format(serializer.data.get('attached'))
        print(attached)
        return ContactInformation(
                    id=serializer.data.get('id'),
                    mensaje=serializer.data.get('mensaje'),
                    register=serializer.data.get('register'),
                    attached=attached,
                    client=Client(id=serializer.data.get('client_id'))) 



    def __str__(self):
        return 'CONTACT: {0}  | {1} | {2} | {3} | {4} |'.format(self.id, self.mensaje, self.register, self.attached, self.client)

    class Meta:
        managed = False
        db_table = 'contact_information'