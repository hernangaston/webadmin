from django.contrib import admin

# Register your models here.
from .models import Corredor


class CorredorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(Corredor, CorredorAdmin)