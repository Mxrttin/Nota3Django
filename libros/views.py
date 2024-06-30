from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Libros
<<<<<<< HEAD
from .forms import SearchForm
=======

>>>>>>> 881105c3acfd9889139c471aef01555f82ccf41d

# Create your views here.


@login_required

def comics(request):
    libros = Libros.objects.all()
    return render(request, "libros/comics.html", {'libros': libros})


@login_required

def mangas(request):
    libros = Libros.objects.all()
    return render(request, "libros/mangas.html",{'libros': libros})


@login_required
def destacados(request):
<<<<<<< HEAD
    context = {}
    return render(request, "libros/destacados.html",context)

def search_view(request):
    form = SearchForm(request.GET or None)
    libros = Libros.objects.all()

    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        escritor = form.cleaned_data.get('escritor')

        if titulo:
            libros = libros.filter(titulo__icontains=titulo)
        if escritor:
            libros = libros.filter(titulo__icontains=escritor)

    return render(request, 'comics.html', {'form': form, 'libros': libros})

    
    
=======
    libros = Libros.objects.all()
    return render(request, "libros/destacados.html",{'libros': libros})

>>>>>>> 881105c3acfd9889139c471aef01555f82ccf41d

