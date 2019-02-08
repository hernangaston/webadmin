from django.urls import path, include
from rest_framework import routers
from .viewsets import EmpresaViewSet, UserViewSet
from .views import ViewEmpresa, CreateEmpresa


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'users', UserViewSet)


urlempresa = [
    path('api/', include(router.urls)),
    path('', ViewEmpresa.as_view()),
    path('create/', CreateEmpresa.as_view()),
]