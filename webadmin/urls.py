"""webadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from empresa.urls import urlempresa
from cartadeporte.urls import urlcp
from intermediario.urls import urlintermediarios
from remitentecomercial.urls import urlremitentecomercial
from intermediarioflete.urls import urlintermediarioflete
from corredor.urls import urlcorredor
from mat.urls import urlmat
from entregador.urls import urlentregador
from destinatario.urls import urldestinatario
from destino.urls import urldestino
from transportista.urls import urltransportista
from chofer.urls import urlchofer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresa/', include(urlempresa)),
    path('cp/', include(urlcp)),
    path('intermediarios/', include(urlintermediarios)),
    path('rem_comercial/', include(urlremitentecomercial)),
    path('corredor/', include(urlcorredor)),
    path('mat/', include(urlmat)),
    path('entregador/', include(urlentregador)),
    path('destinatario/', include(urldestinatario)),
    path('destino/', include(urldestino)),
    path('intermediarioflete/', include(urlintermediarioflete)),
    path('transportista/', include(urltransportista)),
    path('chofer/', include(urlchofer))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
