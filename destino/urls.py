from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .viewsets import DestinoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'list', DestinoViewSet)

app_name = 'destino'
urldestino = [
    path('api/', include(router.urls)),
]