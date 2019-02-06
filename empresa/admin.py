from django.contrib import admin

# Register your models here.
from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']
    list_display = ('nombre', 'cuit', 'user', 'created_at')

admin.site.register(Empresa, EmpresaAdmin)