from rest_framework import serializers
from .models import IntermediarioFlete

class IntermediarioFleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntermediarioFlete
        fields = '__all__'

