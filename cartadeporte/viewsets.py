from rest_framework import viewsets
from .models import CartaDePorte
from .serializers import CartaDePorteSerializer


# ViewSets define the view behavior.
class CartaDePorteViewSet(viewsets.ModelViewSet):
    queryset = CartaDePorte.objects.all()
    serializer_class = CartaDePorteSerializer
    