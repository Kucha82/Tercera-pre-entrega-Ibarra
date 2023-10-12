from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Curso, Familiar, Imagen, User
from .forms import (CursoFormulario, BuscaCursoForm, BuscarFamiliar, UserRegisterform,
                    UserEditForm, MyUserEditForm)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "Appboots/base.html")


def cursos(request):
    return render(request, "Appboots/cursos.html")


@login_required
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


def mostrar_familiar(request):
    pass


def read_cursos(request):

    cursos = Curso.objects.all()  # trae todos los cursos

    contexto = {"cursos": cursos}

    return render(request, "Appboots/readCursos.html", contexto)


def ver_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'Appboots/ver_curso.html', {'curso': curso})


def delete_curso(request, curso_id):

    curso = Curso.objects.get(id=int(curso_id))
    curso.delete()

    # vuelvo al menú
    cursos = Curso.objects.all()  # trae todos los cursos
    return render(request, "Appboots/readCursos.html", {"cursos": cursos})


def edit_curso(request, curso_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            curso = Curso.objects.get(id=curso_id)
            curso.nombre = informacion["curso"]
            curso.camada = informacion["camada"]
            curso.save()

            return render(request, "Appboots/base.html")
    else:
        curso = Curso.objects.get(id=curso_id)
        miFormulario = CursoFormulario(
            initial={"curso": curso.nombre, "camada": curso.camada})

    return render(request, "Appboots/editCurso.html", {"miFormulario": miFormulario})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "Appboots/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "Appboots/login.html", {"mensaje": "Error, datos incorrectos", "form": form})

        else:
            return render(request, "Appboots/base.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Appboots/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appboots/base.html", {"mensaje": f"{username} Usuario Creado ;)"})
    else:
        # form = UserCreationForm()
        form = UserRegisterform(request.POST)

    return render(request, "Appboots/registro.html", {"form": form})


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = MyUserEditForm(request.POST, request.FILES)
        # archivo_form = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():  # and archivo_form.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            # usuario.password1 = informacion['password1']
            # usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # miFormulario.save()
            # perfil.avatar = archivo_form.cleaned_data["avatar"]
            # perfil.save()

            user = User.objects.get(username=request.user)
            try:
                avat = Imagen.objects.get(user=user)
            except Imagen.DoesNotExist:
                avat = Imagen(user=user, imagen=informacion.get("imagen"))
                avat.save()
            else:
                avat.imagen = miFormulario.cleaned_data["avatar"]
                avat.save()

            # archivo_form.save()

            return render(request, "Appboots/base.html")
        else:
            miFormulario = MyUserEditForm()

    else:
        miFormulario = MyUserEditForm(
            initial={
                'email': usuario.email,
                'last_name': usuario.last_name,
                'first_name': usuario.first_name
            }
        )
    return render(request, "Appboots/editUser.html", {"miFormulario": miFormulario,
                                                      "usuario": usuario
                                                      }
                  )


#################################################################################################


class CursoListView(ListView):
    model = Curso
    template_name = "Appboots/listaClass.html"


class CursoDetailView(DetailView):
    queryset = Curso.objects.all()
    template_name = "Appboots/cursoDetalle.html"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "Appboots/cursoEdit.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "camada"]


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "Appboots/cursoEdit.html"
    success_url = reverse_lazy("List")
    # success_url = "Appboots/clases/lista"
    fields = ["nombre", "camada"]


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = "Appboots/cursoDelete.html"
