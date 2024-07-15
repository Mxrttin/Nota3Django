from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .carrito import Carrito
from libros.models import Libros
from .models import Orden , DireccionEnvio
from django.utils import timezone

# Create your views here.


@login_required

def carrito(request):
    libro = Libros.objects.all()
    return render(request, "carrito/carrito.html",{'productos':libro})


def checkout(request):
    return render(request, "carrito/checkout.html")


def agregarProducto(request, libro_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.agregar(libro)
    return redirect("carrito")

def eliminarProducto(request, libro_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.eliminar(libro)
    return redirect("carrito")

def restarProducto(request, libro_id):
    carrito = Carrito(request)
    libro = Libros.objects.get(id=libro_id)
    carrito.restar(libro)
    return redirect("carrito")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


def realizarCompra(request):
    if request.method == 'POST':
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        comuna = request.POST['comuna']
        codigo_postal = request.POST['codigo_postal']


        id_trans = Orden.objects.order_by('transaccion_id').last()

        if id_trans and id_trans.transaccion_id.isdigit():
            id_nuevo = int(id_trans.transaccion_id) + 1
        else :
            id_nuevo = 1


        # crear Orden de compra
        orden = Orden.objects.create(
            cliente = request.user,
            fecha_orden = timezone.now(),
            completo = True,
            transaccion_id=str(id_nuevo)
        )

        
        direccionEnvio = DireccionEnvio.objects.create(
            cliente = request.user,
            Orden = orden,
            direccion = direccion,
            ciudad = ciudad,
            comuna = comuna,
            codigo_postal = codigo_postal,
            fecha_agregado=timezone.now()
        )

        carrito = Carrito(request)
        carrito.limpiar()

    return render (request , "inicio/inicio.html")