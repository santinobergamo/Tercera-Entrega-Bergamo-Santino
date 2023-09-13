# forms.py
from django import forms
from .models import PedidoCompra, Proveedor

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    codigo = forms.CharField(max_length=10)

class PedidoCompraForm(forms.ModelForm):
    class Meta:
        model = PedidoCompra
        fields = ['proveedor', 'fecha_pedido', 'fecha_entrega_esperada', 'nombre_producto', 'codigo_producto', 'cantidad', 'precio_unitario']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']
