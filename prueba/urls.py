from django.urls import path
from prueba.views import prueba, herenciaHijo2, index

urlpatterns = [
    path('index/', index, name='index'),
    path('cursos/', prueba, name='cursos'),
    path('recetas/', herenciaHijo2, name='recetas'),
]