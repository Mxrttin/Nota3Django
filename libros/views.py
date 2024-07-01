from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Libros
from .forms import SearchForm

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


def search_view(request):
    form = SearchForm(request.GET or None)
    libros = []

    if form.is_valid():
        libros = form.filter_libros()

    context = {
        'form': form,
        'libros': libros,
    }
    
    if form.cleaned_data.get('tipo') == 'manga':
        return render(request, 'mangas.html', context)
    else:
        return render(request, 'comics,html', context)

       

    
    
  


