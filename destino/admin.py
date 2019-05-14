from django.contrib import admin

# Register your models here.
from .models import Destino


class DestinoAdmin(admin.ModelAdmin):
    fields = ['destinatario', 'nombre', 'cuit', 'codigo_de_planta', 'direccion', 'localidad', 'provincia']

admin.site.register(Destino, DestinoAdmin)