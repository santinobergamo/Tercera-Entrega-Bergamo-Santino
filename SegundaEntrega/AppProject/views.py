from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Producto, PedidoCompra
from .forms import ProductoFormulario, PedidoCompraForm

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
            return render(req, "index.html")
    else:
        formulario = ProductoFormulario()

    return render(req, "formulario.html", {"formulario": formulario})


def buscar(req):
    codigo = req.GET.get("codigo")
    if codigo:
        try:
            buscar_producto = Producto.objects.get(codigo=codigo)
            return render(req, "resultadosBusqueda.html", {"productos": [buscar_producto]})
        except Producto.DoesNotExist:
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

        producto = Producto.objects.all()

        return render(req, "listaProductos.html", {"productos" : productos})


def crear_pedido_compra(request):
    if request.method == 'POST':
        pedido_form = PedidoCompraForm(request.POST)
        if pedido_form.is_valid():
            pedido = pedido_form.save()
            return redirect('lista_pedidoscompra')
    else:
        pedido_form = PedidoCompraForm()
    return render(request, 'crear_pedido_compra.html', {'pedido_form': pedido_form})


def lista_pedidos_compra(request):
    pedidos = PedidoCompra.objects.all()
    return render(request, 'lista_pedidoscompra.html', {'pedidos': pedidos})







# Create your views here.
