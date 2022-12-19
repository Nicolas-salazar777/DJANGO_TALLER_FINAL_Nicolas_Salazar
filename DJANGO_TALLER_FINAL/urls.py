"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AppSeminario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('Seminario/',views.listadodeinscritos),
    path('agregarinscripcion',views.ingresodeinscritos),
    path('actualizar/<int:id>',views.modificacióndeinscritos),
    path('eliminar/<int:id>',views.eliminacióndeinscritos),
    path('inscriptosDB/', views.verinscriptosDb),
    
    #Class Based Views
    path('ListarInscritos/', views.ListarSeminario.as_view()),
    path('ListarInscritos/<int:pk>', views.DetalleSeminario.as_view()),
    
    #Función Based Views
    path('ListarInstitucion/', views.seminario_list),
    path('ListarInstitucion/<int:pk>', views.seminario_detalle),
]
