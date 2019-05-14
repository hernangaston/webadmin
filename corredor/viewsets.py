from rest_framework import viewsets
from .models import Corredor
from .serializers import CorredorSerializer

# ViewSets define the view behavior.
class CorredorViewSet(viewsets.ModelViewSet):
    queryset = Corredor.objects.all()
    serializer_class = CorredorSerializer


    