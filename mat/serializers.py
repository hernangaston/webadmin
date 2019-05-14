from rest_framework import serializers
from .models import MercadoATermino

class MercadoATerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MercadoATermino
        fields = '__all__'

