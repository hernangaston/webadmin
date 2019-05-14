from django.contrib import admin

# Register your models here.
from .models import MercadoATermino


class MercadoATerminoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(MercadoATermino, MercadoATerminoAdmin)