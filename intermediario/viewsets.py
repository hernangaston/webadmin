from rest_framework import viewsets
from .models import Intermediario
from .serializers import IntermediarioSerializer

# ViewSets define the view behavior.
class IntermediarioViewSet(viewsets.ModelViewSet):
    queryset = Intermediario.objects.all()
    serializer_class = IntermediarioSerializer


    