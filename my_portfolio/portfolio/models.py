from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    imagen=models.ImageField(("Imagen"), upload_to='images/', height_field=None, width_field=None, max_length=None)
    

    def __str__(self):
        
        return f"Usuario: {self.username}, Nombre: {self.first_name}, Apellido: {self.last_name}, en el sistema desde: {self.date_joined}"
    
    
    
class Educacion(models.Model):
    
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    lugar=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(("Imagen"), upload_to='images/', height_field=None, width_field=None, max_length=None)

    
class Proyectos(models.Model):
    
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    lugar=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(("Imagen"), upload_to='images/', height_field=None, width_field=None, max_length=None)


class Experiencia(models.Model):
    
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    lugar=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(("Imagen"), upload_to='images/', height_field=None, width_field=None, max_length=None)
    
class Servicios(models.Model):
    
    descripcion=models.CharField(max_length=400)
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(("Imagen"), upload_to='images/', height_field=None, width_field=None, max_length=None)