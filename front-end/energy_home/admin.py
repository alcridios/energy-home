from django.contrib import admin
from persistence.models import Client, ContactInformation

admin.site.register(Client)
admin.site.register(ContactInformation)