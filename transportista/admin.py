from django.contrib import admin

# Register your models here.
from .models import Transportista


class TransportistaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(Transportista, TransportistaAdmin)