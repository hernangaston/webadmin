from rest_framework import viewsets
from .models import MercadoATermino
from .serializers import MercadoATerminoSerializer

# ViewSets define the view behavior.
class MercadoATerminoViewSet(viewsets.ModelViewSet):
    queryset = MercadoATermino.objects.all()
    serializer_class = MercadoATerminoSerializer


    