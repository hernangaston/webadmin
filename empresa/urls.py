from django.urls import path, include
from .views import ViewEmpresa

urlempresa = [
    path('empresa/', ViewEmpresa.as_view()),
]