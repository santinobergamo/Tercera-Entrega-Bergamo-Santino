from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Producto, PedidoCompra, Proveedor
from .forms import ProductoFormulario, PedidoCompraForm, ProveedorForm

#Base de datos!

def index(req):

    return render(req, 'index.html')


def productos(req):

    productos = Producto.objects.all()

    return render(req, "listaProductos.html", {"productos": productos})


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
            
            pedido = pedido_form.save(commit=False)
            proveedor_id = request.POST.get('proveedor_id')
            nombre_nuevo_proveedor = request.POST.get('nombre_nuevo_proveedor')

            if proveedor_id:
                pedido.proveedor = Proveedor.objects.get(pk=proveedor_id)
            elif nombre_nuevo_proveedor:
                nuevo_proveedor = Proveedor.objects.create(nombre=nombre_nuevo_proveedor)
                pedido.proveedor = nuevo_proveedor

            pedido.save()
            return redirect('lista_pedidoscompra')
    else:
        pedido_form = PedidoCompraForm()

    return render(request, 'crear_pedido_compra.html', {'pedido_form': pedido_form, 'proveedores': Proveedor.objects.all()})


def lista_pedidos_compra(request):
    pedidos = PedidoCompra.objects.all()
    return render(request, 'lista_pedidoscompra.html', {'pedidos': pedidos})

def crear_proveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor = proveedor_form.save()
            return redirect('crear_pedido_compra')  # Después de crear el proveedor, redirige al usuario a la vista de creación de pedidos de compra
    else:
        proveedor_form = ProveedorForm()

    return render(request, 'crear_proveedor.html', {'proveedor_form': proveedor_form})


def editar_pedido_compra(request, pedido_id):
    pedido = PedidoCompra.objects.get(id=pedido_id)

    if request.method == 'POST':
        # Obtiene los datos del formulario
        fecha_pedido = request.POST.get('fecha_pedido')
        fecha_entrega_esperada = request.POST.get('fecha_entrega_esperada')
        
        # Actualiza los campos del pedido
        pedido.fecha_pedido = fecha_pedido
        pedido.fecha_entrega_esperada = fecha_entrega_esperada
        pedido.save()
  
        return redirect('lista_pedidoscompra')  

    return render(request, 'editar_pedido_compra.html', {'pedido': pedido})


def eliminar_pedido_compra(req, pedido_id):
        
        pedido = PedidoCompra.objects.get(id=pedido_id)
        if req.method == 'POST':

            pedido = PedidoCompra.objects.get(id=id)
            pedido.delete()

            pedido = Producto.objects.all()

            return render(req, "lista_pedidoscompra")

        return render(req, 'eliminar_pedido_compra.html', {'pedido': pedido})


