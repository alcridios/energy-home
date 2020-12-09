from django.db import models


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rut = models.CharField(db_column='RUT', unique=True, max_length=18)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return 'ID:{0} RUT: {1} -> NOMBRE: {2} {3} -> EMAIL: {4} TELEFONO: {5}'.format(self.id, self.rut, self.nombre, self.direccion,  self.email, self.telefono)

    class Meta:
        managed = False
        db_table = 'client'


    def json_serializer(self):
        return {
                'id': self.id,
                'rut': self.rut,
                'nombre': self.nombre,
                'direccion': self.direccion,
                'email': self.email,
                'telefono': self.telefono}
    

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
    attached = models.ImageField(db_column='UPLOAD_IMAGE', upload_to='contacts')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_ID', blank=True, null=True)  # Field name made lowercase.

    @property
    def image_url(self):
        from django.contrib.sites.models import Site
        domain = Site.objects.get_current().domain
        url = 'http://{domain}'.format(domain=domain)

        if self.attached and hasattr(self.attached, 'url'):
            return url + self.attached.url

    def __str__(self):
        return 'CONTACT: {0} - REGISTER: {1} | {2}'.format(self.mensaje, self.register, self.client)

    class Meta:
        managed = False
        db_table = 'contact_information'
