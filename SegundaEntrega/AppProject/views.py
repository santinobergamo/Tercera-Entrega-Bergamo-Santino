from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import ProductoFormulario

#Base de datos!

def producto(req, producto, codigo):

    productos = Producto(NombreProducto=producto, codigo=codigo)
    productos.save()

def index(req):

    return render(req, 'index.html')


def productos(req):

    return render(req, "productos.html")

def carrito(req):

    return render(req, "carrito.html")


def prodFormulario(req):
    if req.method == 'POST':
        formulario = ProductoFormulario(req.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto = Producto(nombre=data["NombreProducto"], codigo=data["codigo"])
            producto.save()
            return render(req, 'index.html')
    else:
        formulario = ProductoFormulario()  

    return render(req, "formulario.html", {"formulario": formulario})

# Create your views here.
