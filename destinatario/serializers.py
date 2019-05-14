from rest_framework import serializers
from .models import Destinatario

class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = '__all__'

