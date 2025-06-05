
from django.urls import path
from . import views
urlpatterns=[
    
    path('inicio',views.inicio,name='inicio'),
    path('nuevoMonumento', views.nuevoMonumento),
    path('guardarMonumento', views.guardarMonumento),
    path('eliminarMonumento/<id>', views.eliminarMonumento),
    path('editarMonumento/<id>', views.editarMonumento),
    path('procesarEdicionMonumento',views.procesarEdicionMonumento)
    
]