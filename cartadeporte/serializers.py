from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CartaDePorte

# DEFINIMOS QUE CAMPOS VAMOS A UTILIZAR DE NUESTRO MODELO

class CartaDePorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaDePorte
        fields = (
                'id',
                'pk',
                'numero',
                'conforme',
                'fecha',
                'intermediario',
                'ctg',
                'renspa',
                'conforme',
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
                'contrato',
                'pesada_en_destino',
                'kgs_estimados',
                'declaracion_calidad',
                'condicional',
                'peso_bruto',
                'peso_tara',
                'peso_neto',
                'observaciones',
                'direccion_procedencia',
                'localidad_procedencia',
                'provincia_procedencia',
                'kilometros',
                'tarifa',
                'tarifa_referencia',
                'declaracion_juarada_nombre',
                'declaracion_juarada_dni',
                'docfile'
                )

class CartaDePorteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaDePorte
        fields = '__all__'

