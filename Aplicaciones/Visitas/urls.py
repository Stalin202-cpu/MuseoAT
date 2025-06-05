#Configuracion de rutas especificas de la aplicacion empresas
from django.urls import path 
from . import views
urlpatterns=[
    path('inicio2',views.inicio2, name='inicio2'),
    path('nuevaVisita', views.nuevaVisita),
    path('guardarVisita', views.guardarVisita),
    path('eliminarVisita/<id>', views.eliminarVisita),
    path('editarVisita/<id>', views.editarVisita),
    path('procesarEdicionVisita', views.procesarEdicionVisita),
]