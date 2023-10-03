from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class BuscaCursoForm(forms.Form):
    curso = forms.CharField()


class BuscarFamiliar(forms.Form):
    parentesco = forms.CharField()
