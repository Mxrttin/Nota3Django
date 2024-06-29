from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required

def comics(request):
    context = {}
    return render(request, "libros/comics.html",context)


@login_required

def mangas(request):
    context = {}
    return render(request, "libros/mangas.html",context)


@login_required
def destacados(request):
    context = {}
    return render(request, "libros/destacados.html",context)
