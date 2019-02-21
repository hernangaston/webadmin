from django.urls import path, include
from rest_framework import routers
from .viewsets import EmpresasViewSet, UsersViewSet, UserAuthViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresas', EmpresasViewSet)
router.register(r'users', UsersViewSet)
router.register(r'auth', UserAuthViewSet)


urlempresa = [
    path('', include(router.urls)),
]