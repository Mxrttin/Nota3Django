from django import forms

class SearchForm(forms.Form):
    titulo = forms.CharField(label='Titulo', required=False)
    escritor = forms.CharField(label='Escritor', required=False)


    