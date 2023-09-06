from django import forms

class ProductoFormulario(forms.Form):

    NombreProducto = forms.CharField(max_length=40)
    codigo = forms.IntegerField()