from django.contrib import admin

# Register your models here.
from .models import IntermediarioFlete


class IntermediarioFleteAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(IntermediarioFlete, IntermediarioFleteAdmin)