from django.urls import path
from .views import (inicio, saludo, hora, cursos, guitarra, lista,
                    cursoFormulario, buscarCurso, buscarFamiliar)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('saludo/', saludo, name="Saludo"),
    path('hora/', hora, name="Hora"),
    path('curso/', cursos, name="Cursos"),
    path('guitarra/', guitarra, name="Guitarra"),
    path('lista/', lista, name="Lista"),
    path('formCurso/', cursoFormulario, name="cursoFormulario"),
    path('buscarCurso/', buscarCurso, name="BuscarCurso"),
    path('buscarFamiliar/', buscarFamiliar, name="BuscarFamiliar")
]
