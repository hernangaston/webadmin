from django.contrib import admin

# Register your models here.
from .models import Destinatario


class DestinatarioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(Destinatario, DestinatarioAdmin)