from django.contrib import admin

# Register your models here.
from .models import Intermediario


class IntermediarioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(Intermediario, IntermediarioAdmin)