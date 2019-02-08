from rest_framework import viewsets
from .models import Empresa, Usuario
from .serializers import EmpresaSerializer, UserSerializer

# ViewSets define the view behavior.
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
