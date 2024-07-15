from django.db import models 
from django.contrib.auth.models import User
from libros.models import Libros

# Create your models here.

class Orden(models.Model):
    cliente = models.ForeignKey(User , on_delete = models.SET_NULL, blank = True , null = True)
    fecha_orden = models.DateTimeField(auto_now_add = True)
    completo = models.BooleanField(default = False , null = True ,  blank = False)
    transaccion_id = models.CharField(max_length = 200 , null = True)

    def __str__(self):
        return str(self.transaccion_id)


class DireccionEnvio (models.Model):
    cliente = models.ForeignKey(User , on_delete = models.SET_NULL, blank = True , null = True)
    Orden = models.ForeignKey(Orden , on_delete = models.SET_NULL , blank = True , null = True)
    direccion = models.CharField(max_length = 200 , null = True)
    ciudad = models.CharField(max_length = 200 , null = True)
    comuna = models.CharField(max_length = 200 , null = True)
    codigo_postal = models.CharField(max_length = 200 , null = True)
    fecha_agregado = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.direccion


class ProductosComprados(models.Model):
    Orden = models.ForeignKey(Orden , on_delete = models.SET_NULL , blank = True , null = True)
    titulo = models.ForeignKey(Libros, on_delete=models.SET_NULL,blank = True , null= True)
    cantidad = models.IntegerField( default = 0,blank = True , null= True)

    def __str__(self):
        return str(self.Orden)

