from rest_framework import serializers
from .models import Intermediario

class IntermediarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intermediario
        fields = '__all__'

