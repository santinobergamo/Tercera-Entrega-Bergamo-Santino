from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10)

class PedidoCompra(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    fecha_entrega_esperada = models.DateField()
    detalles = models.ManyToManyField('Producto', through='DetallePedidoCompra')

    def __str__(self):
        return f'Pedido de compra #{self.id} - Proveedor: {self.proveedor}'

class DetallePedidoCompra(models.Model):
    pedido = models.ForeignKey(PedidoCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f'Detalle del pedido #{self.pedido.id} - Producto: {self.producto}'
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    # Otros campos relevantes para el proveedor

    def __str__(self):
        return self.nombre




# Create your models here.
