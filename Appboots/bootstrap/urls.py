from django.urls import path
from .views import (inicio, saludo, hora)

urlpatterns = [
    path('inicio/', inicio),
    path('saludo/', saludo),
    path('hora/', hora),
]
