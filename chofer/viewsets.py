from rest_framework import viewsets
from .models import Chofer
from .serializers import ChoferSerializer

# ViewSets define the view behavior.
class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer


    