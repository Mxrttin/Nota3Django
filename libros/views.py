from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Libros


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
    libros = Libros.objects.all()
    return render(request, "libros/destacados.html",{'libros': libros})


