from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10)

class BuscarProducto(models.Model):
    codigo = models.CharField(max_length=40)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)


class IngresarProdcuto (models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)

# Create your models here.
