from rest_framework import viewsets
from .models import Destino
from .serializers import DestinoSerializer

# ViewSets define the view behavior.
class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer


    