from rest_framework import viewsets
from .models import Entregador
from .serializers import EntregadorSerializer

# ViewSets define the view behavior.
class EntregadorViewSet(viewsets.ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer


    