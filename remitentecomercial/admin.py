from django.contrib import admin

# Register your models here.
from .models import RemitenteComercial


class RemitenteComercialAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cuit']

admin.site.register(RemitenteComercial, RemitenteComercialAdmin)