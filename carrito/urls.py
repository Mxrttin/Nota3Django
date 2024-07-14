from django.urls import path 
from. import views  
from .views import agregarProducto,eliminarProducto,restarProducto,limpiarCarrito,realizarCompra

urlpatterns = [
    path('carrito',views.carrito , name="carrito"),
    path('agregar/<int:libro_id>', agregarProducto , name='Add'),
    path('eliminar/<int:libro_id>', eliminarProducto , name='Eliminar'),
    path('restar/<int:libro_id>', restarProducto , name='Restar'),
    path('limpiar/', limpiarCarrito , name='Limpiar'),
    path('checkout/', views.checkout , name='checkout') ,
    path('realizar_compra/', realizarCompra , name='realizar_compra') ,

]