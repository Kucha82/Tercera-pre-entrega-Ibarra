from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"Curso: {self.nombre} - Camada: {self.camada}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    apellido = models.CharField(max_length=30)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()


class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=200)
    parentesco = models.CharField(max_length=15)
    edad = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Parentesco: {self.parentesco}"


class Imagen(models.Model):
    # vinvulo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    # def d(self):
    #     return self.user.last_name

    def __str__(self):
        return f"media/{self.imagen}"
