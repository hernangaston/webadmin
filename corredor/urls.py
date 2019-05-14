from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .viewsets import CorredorViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'list', CorredorViewSet)

app_name = 'corredor'
urlcorredor = [
    path('api/', include(router.urls)),
]