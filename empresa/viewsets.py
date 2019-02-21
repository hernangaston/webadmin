from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Empresa, Usuario
from .serializers import EmpresaSerializer, UserSerializer, UserAuthSerializer

# ViewSets define the view behavior.
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer


    