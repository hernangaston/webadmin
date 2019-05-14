from rest_framework import viewsets
from .models import Transportista
from .serializers import TransportistaSerializer

# ViewSets define the view behavior.
class TransportistaViewSet(viewsets.ModelViewSet):
    queryset = Transportista.objects.all()
    serializer_class = TransportistaSerializer


    