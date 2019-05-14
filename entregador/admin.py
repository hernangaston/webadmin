from django.contrib import admin

# Register your models here.
from .models import Entregador


class EntregadorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(Entregador, EntregadorAdmin)