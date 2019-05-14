from django.contrib import admin

# Register your models here.
from .models import Chofer


class ChoferAdmin(admin.ModelAdmin):
    fields = ['transportista','nombre', 'apellido', 'cuit', 'patente_chasis', 'patente_acoplado']

admin.site.register(Chofer, ChoferAdmin)