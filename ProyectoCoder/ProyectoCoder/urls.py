"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from ProyectoCoderApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('crearpython/',crear_curso),
    path('coderapp/',include('ProyectoCoderApp.urls')), #en esta linea le indicamos que vaya a la app, e importe todas las urls!!!!!!!
    #path('auth/',include('auth.urls')), #estas podrían ser las URLS de autenticación si las tuviésemos. También irian acá en la carpeta ppal.
]

#muchas aplicaciones
#profes, estu, cursos, entregables+

#chat
#mensajes, canales, fijados 

#Todo esto nos obligaria a crear MUCHAS URLS, entonces en cambio creamos  en una linea todas las URLS de la app (línea 25).