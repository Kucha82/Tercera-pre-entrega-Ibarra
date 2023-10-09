from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class BuscaCursoForm(forms.Form):
    curso = forms.CharField()


class BuscarFamiliar(forms.Form):
    parentesco = forms.CharField()


class UserRegisterform(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
