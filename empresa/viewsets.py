from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Empresa
from .serializers import EmpresaSerializer, UserAuthSerializer

# ViewSets define the view behavior.
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# ViewSets define the view behavior.
class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer


    