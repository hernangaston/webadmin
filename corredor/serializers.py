from rest_framework import serializers
from .models import Corredor

class CorredorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corredor
        fields = '__all__'

