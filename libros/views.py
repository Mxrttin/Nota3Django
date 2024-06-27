from django.shortcuts import render

# Create your views here.

def comics(request):
    context = {}
    return render(request, "libros/comics.html",context)


def mangas(request):
    context = {}
    return render(request, "libros/mangas.html",context)


def destacados(request):
    context = {}
    return render(request, "libros/destacados.html",context)
