from rest_framework import serializers
from .models import Empresa, Usuario

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('pk','id', 'user', 'nombre', 'cuit', 'created_at', 'updated_at', 'nombreUser')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')