from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Libros
# from .forms import SearchForm
from django.db.models import Q

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



       
@login_required
def buscar(request):
    busqueda= request.GET.get("buscar")
    libros = Libros.objects.all()


    if busqueda:
        libros=Libros.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(escritor__icontains = busqueda) |
            Q(id_serie__serie__icontains = busqueda) 
        ).distinct()

    return render(request,"libros/busqueda.html",{'libros':libros})

    
    
  


