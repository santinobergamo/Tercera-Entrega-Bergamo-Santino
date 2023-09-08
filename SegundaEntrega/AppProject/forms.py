from django import forms

class ProductoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()

