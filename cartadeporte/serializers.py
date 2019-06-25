from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CartaDePorte

class CartaDePorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaDePorte
        fields = '__all__'

class CartaDePorteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaDePorte
        fields = '__all__'

