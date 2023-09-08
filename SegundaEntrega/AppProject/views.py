from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import ProductoFormulario

#Base de datos!

def index(req):

    return render(req, 'index.html')


def productos(req):

    productos = Producto.objects.all()

    return render(req, "listaProductos.html", {"productos": productos})


def carrito(req):

    return render(req, "carrito.html")


def prodFormulario(req):
    if req.method == 'POST':
        formulario = ProductoFormulario(req.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto = Producto(nombre=data["nombre"], codigo=data["codigo"])
            producto.save()
            return render(req, 'index.html')
    else:
        formulario = ProductoFormulario()  

    return render(req, "formulario.html", {"formulario": formulario})


def buscar(req):
    codigo = req.GET.get("codigo")  
    if codigo:
        productos = Producto.objects.filter(codigo=codigo)
        if productos.exists():
            return render(req, "resultadosBusqueda.html", {"productos": productos})
        else:
            return HttpResponse('No se encontró ningún producto con ese código')
    else:
        return HttpResponse('Debe agregar un código de producto')


def busquedaProducto(req):
    
    return render (req, "resultadosBusqueda.html")


def mostrar_formulario_busqueda(req):
    return render(req, 'formulario_busqueda.html')


def editarProducto(req, id):
    try:
        producto = Producto.objects.get(id=id)

        if req.method == 'POST':
            miFormulario = ProductoFormulario(req.POST)
            if miFormulario.is_valid(): 
                data = miFormulario.cleaned_data
                producto.nombre = data["nombre"]
                producto.codigo = data["codigo"]
                producto.save()
                return render(req, "index.html")
        else:
            miFormulario = ProductoFormulario(initial={
                "nombre": producto.nombre,
                "codigo": producto.codigo,
            })
            return render(req, "editarProducto.html", {"miFormulario": miFormulario, "id": producto.id})  
    except Producto.DoesNotExist:
        return HttpResponse('No se encontró ningún producto con ese ID')

    
def eliminarProducto(req, id):

    if req.method == 'POST':

        producto = Producto.objects.get(id=id)
        producto.delete()

        profesores = Producto.objects.all()

        return render(req, "listaProductos.html", {"productos" : productos})







# Create your views here.
