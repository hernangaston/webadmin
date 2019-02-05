from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ('__all__')