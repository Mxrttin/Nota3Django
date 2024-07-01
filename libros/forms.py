from django import forms
from .models import Libros

class SearchForm(forms.Form):
    titulo = forms.CharField(label='Titulo', required=False)
    escritor = forms.CharField(label='Escritor', required=False)

    def filter_libros(self):
        libros = Libros.objects.all()

        titulo = self.cleaned_data.get('Titulo')
        if titulo:
            libros = Libros.filter(titulo_incontains=titulo)

        escritor = self.cleaned_data.get('Escritor')
        if escritor:
            libros = Libros.filter(escritor_icontains=escritor)

        return libros   
    


    