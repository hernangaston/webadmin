from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('pk','id', 'nombre', 'cuit', 'created_at', 'updated_at')

# Serializers define the API representation.
class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')