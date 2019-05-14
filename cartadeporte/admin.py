from django.contrib import admin

# Register your models here.
from .models import CartaDePorte


class CartaDePorteAdmin(admin.ModelAdmin):
    fields = [
        'numero',
        'ctg',
        'renspa',
        'fecha',
        'intermediario',
        'remitente_comercial',
        'corredor_comprador',
        'mercado_a_termino',
        'corredor_vendedor',
        'entregador',
        'destinatario',
        'destino',
        'intermediario_flete',
        'transportista',
        'chofer',
        'grano',
        'tipo',
        'cosecha',
        'contrato', #aca enlazamos con los ctos. de compra vta.
        'pesada_en_destino',
        'kgs_estimados',
        'declaracion_calidad',
        'conforme',
        'condicional',
        'peso_bruto',
        'peso_tara',
        'peso_neto',
        'observaciones',
        #-----------------PROCEDENCIA-----------------------
        'direccion_procedencia',
        'localidad_procedencia',
        'provincia_procedencia',
        'kilometros',
        'tarifa',
        'tarifa_referencia',
        'declaracion_juarada_nombre',
        'declaracion_juarada_dni',
        'docfile',
    ]

admin.site.register(CartaDePorte, CartaDePorteAdmin)