from django.urls import path
from .views import (inicio, saludo, hora, cursos, guitarra)

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('saludo/', saludo, name="Saludo"),
    path('hora/', hora, name="Hora"),
    path('curso/', cursos, name="Cursos"),
    path('guitarra/', guitarra, name="Guitarra")
]
