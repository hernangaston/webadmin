from rest_framework import serializers
from .models import Chofer

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'

