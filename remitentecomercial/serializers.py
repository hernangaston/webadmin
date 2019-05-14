from rest_framework import serializers
from .models import RemitenteComercial

class RemitenteComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemitenteComercial
        fields = '__all__'

