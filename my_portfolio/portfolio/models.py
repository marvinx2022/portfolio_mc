from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    def __str__(self):
        
        return f"Usuario: {self.username}, Nombre: {self.first_name}, Apellido: {self.last_name}, en el sistema desde: {self.date_joined}"