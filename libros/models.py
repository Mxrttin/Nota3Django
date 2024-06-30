from django.db import models

# Create your models here.


class Serie(models.Model):
    id_serie = models.AutoField(db_column="id_genero",primary_key=True)
    serie = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return str(self.serie)


class Libros(models.Model):
    id=models.CharField(primary_key=True , max_length=5)
    id_serie = models.ForeignKey("Serie", on_delete=models.CASCADE, db_column="id_serie") 
    titulo=models.CharField(max_length=100)
    publicacion=models.DateField(blank=False,null=False)
    escritor=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=700)
    imagen=models.ImageField(upload_to="libros",null=True)
    precio=models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + " " + str(self.id_serie) + " " + str(self.titulo)+ " " + str(self.escritor)

