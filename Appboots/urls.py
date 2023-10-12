from django.urls import path
from .views import (
    inicio, saludo, hora, cursos, guitarra, lista, cursoFormulario,
    buscarCurso, buscarFamiliar, read_cursos, delete_curso, edit_curso, login_request,
    register, ver_curso, editarPerfil
)
from django.contrib.auth.views import LogoutView
from .views import (CursoCreateView, CursoListView, CursoDeleteView, CursoUpdateView,
                    CursoDetailView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('saludo/', saludo, name="Saludo"),
    path('hora/', hora, name="Hora"),
    path('curso/', cursos, name="Cursos"),
    path('guitarra/', guitarra, name="Guitarra"),
    path('lista/', lista, name="Lista"),
    path('formCurso/', cursoFormulario, name="cursoFormulario"),
    path('buscarCurso/', buscarCurso, name="BuscarCurso"),
    path('buscarFamiliar/', buscarFamiliar, name="BuscarFamiliar"),
    path('readCursos/', read_cursos, name="ReadCursos"),
    path('deleteCurso/<int:curso_id>', delete_curso, name="DeleteCurso"),
    path('editCurso/<int:curso_id>', edit_curso, name="EditCurso"),
    path('verCurso/<int:curso_id>', ver_curso, name="VerCurso"),
    path('login/', login_request, name="Login"),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(
        template_name='Appboots/logout.html'), name='Logout'),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('clases/lista/', CursoListView.as_view(), name="List"),
    path('clases/detalle/<pk>/', CursoDetailView.as_view(), name="Detail"),
    path('clases/nuevo/', CursoCreateView.as_view(), name="Create"),
    path('clases/editar/<pk>/', CursoUpdateView.as_view(), name="Edit"),
    path('clases/eliminar/<pk>/', CursoDeleteView.as_view(), name="Delete"),
]
