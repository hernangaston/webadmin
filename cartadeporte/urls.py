from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .viewsets import CartaDePorteViewSet
from .views import CartaDePorteListView, GeneratePDF, simple_upload, CartaDePorteView
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cartas', CartaDePorteViewSet)


app_name = 'CartaDePorte'
urlcp = [
    path('api/', include(router.urls)),
    path('cartaslist/', CartaDePorteListView.as_view(), name="cplist"),
    path('cartaslist/generarpdf/<int:numero>', GeneratePDF.as_view(), name="pdfcp"),
    path('upload/', simple_upload, name="upload"),
    path('subir/', CartaDePorteView.as_view(), name="subir"),
]