from django import forms
from .models import *

class ProductoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()

class PedidoCompraForm(forms.ModelForm):
    class Meta:
        model = PedidoCompra
        fields = ['proveedor', 'fecha_pedido', 'fecha_entrega_esperada']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_pedido'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_entrega_esperada'].widget.attrs['class'] = 'datepicker'