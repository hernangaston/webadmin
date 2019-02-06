from django.shortcuts import render
from django.views.generic import ListView
from .models import Empresa


# Create your views here.
class ViewEmpresa(ListView):
    template_name="index.html"
    model = Empresa