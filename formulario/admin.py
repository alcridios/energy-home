from django.contrib import admin

from formulario.models import datos

# Register your models here.

class datosadmin(admin.ModelAdmin):
    list_display=("nombre", "comuna", "fono")
    search_fields=("nombre", "comuna")
    list_filter=("comuna",)


admin.site.register(datos, datosadmin)
