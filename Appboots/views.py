from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Curso, Familiar
from .forms import CursoFormulario, BuscaCursoForm, BuscarFamiliar


def inicio(request):
    return render(request, "Appboots/base.html")


def cursos(request):
    return render(request, "Appboots/cursos.html")


def guitarra(request):
    return render(request, "Appboots/guitarra.html")


def saludo(request):
    return HttpResponse("helloo")


def hora(request):
    now = datetime.now()
    formatted_time = now.strftime("%A %d/%m/%y %H:%M:%S")
    return HttpResponse(formatted_time)


def lista(request):
    familiares = [
        {"nombre": "Walter", "apellido": "Ibarra",
            "parentesco": "Padre", "edad": 66},
        {"nombre": "Aida", "apellido": "Acuña", "parentesco": "Madre", "edad": 67},
        {"nombre": "Alejandro", "apellido": "Ibarra",
         "parentesco": "hermano", "edad": 32},
        {"nombre": "Favio", "apellido": "Ibarra",
         "parentesco": "hermano", "edad": 35},
        {"nombre": "Marcela", "apellido": "Ibarra",
            "parentesco": "hermana", "edad": 48},
        {"nombre": "Belen", "apellido": "Ibarra",
            "parentesco": "hermana", "edad": 39},
        {"nombre": "Orlando", "apellido": "Ibarra",
            "parentesco": "hermano", "edad": 46},
        {"nombre": "Vicente", "apellido": "Ibarra", "parentesco": "yo", "edad": 40},
        {"nombre": "Nahuel", "apellido": "Ibarra",
            "parentesco": "hijo", "edad": 13},
    ]
    return render(request, "Appboots/familiares.html", {'familiares': familiares})


def cursoFormulario(request):

    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'],
                      camada=request.POST['camada'])
        curso.save()

        return render(request, "Appboots/base.html")

    return render(request, "Appboots/cursoFormulario.html")


def apiCursoFormulario(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(
                nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()
            return render(request, "Appboots/base.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "Appboots/apiCursoFormulario.html", {"miFormulario": miFormulario})


def buscarCurso(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = BuscaCursoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos = Curso.objects.filter(
                nombre__icontains=informacion["curso"])

            return render(request, "Appboots/lista.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "Appboots/apiCursoFormulario.html", {"miFormulario": miFormulario})


def mostrar(request):

    pass


def buscarFamiliar(request):
    if request.method == "POST":

        miFormulario = BuscarFamiliar(request.POST)

        if miFormulario.is_valid():
            parentesco = miFormulario.cleaned_data["parentesco"]
            familiares = Familiar.objects.filter(
                parentesco__icontains=parentesco)
            return render(request, "Appboots/listaApiFamiliar.html", {"familiares": familiares})

    else:
        miFormulario = BuscarFamiliar()

    return render(request, "Appboots/apiCursoFormulario.html", {"miFormulario": miFormulario})


def mostrar_familiar(request, ):
    pass
