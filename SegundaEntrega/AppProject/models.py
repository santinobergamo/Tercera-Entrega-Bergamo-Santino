from django.db import models

class Producto (models.Model):
    
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)

class Usuario (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class Orden (models.Model):
    NumerodeOrden = models.CharField(max_length=10)

# Create your models here.
