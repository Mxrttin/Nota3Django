from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .carrito import Carrito
from libros.models import Libros

# Create your views here.


@login_required

def carrito(request):
    libro = Libros.objects.all()
    return render(request, "carrito/carrito.html",{'productos':libro})




def agregarProducto(request, libro_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.agregar(libro)
    return redirect("carrito")

def eliminarProducto(request, producto_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.eliminar(libro)
    return redirect("carrito")

def restarProducto(request, producto_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.restar(libro)
    return redirect("carrito")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")