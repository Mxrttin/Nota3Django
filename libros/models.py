from django.db import models

# Create your models here.

class Libros(models.Model):
    id=models.CharField(primary_key=True , max_length=5)
    serie=models.CharField(max_length=50) 
    titulo=models.CharField(max_length=100)
    publicacion=models.DateField(blank=False,null=False)
    escritor=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to="libros",null=True)
    precio=models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + " " + str(self.serie) + " " + str(self.titulo)+ " " + str(self.escritor)

