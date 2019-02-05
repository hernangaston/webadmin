from rest_framework import viewsets
from .models import Empresa
from .serializers import EmpresaSerializer

# ViewSets define the view behavior.
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer