from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('formulario/', views.prodFormulario, name='prodFormulario'),
    path('buscarProducto/', views.buscar, name='buscarProducto'),
    path('resultadoBusqueda/', views.busquedaProducto, name='resultadoBusqueda'),
    path('mostrarFormularioBusqueda/', views.mostrar_formulario_busqueda, name='mostrarFormularioBusqueda'),
    path('editarProducto/<int:id>/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('crear_pedido_compra/', views.crear_pedido_compra, name='crear_pedido_compra'),
    path('lista_pedidos_compra/', views.lista_pedidos_compra, name='lista_pedidoscompra'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('editar_pedido_compra/<int:pedido_id>/', views.editar_pedido_compra, name='editar_pedido_compra'),
    path('eliminar_pedido_compra/<int:id>/', views.eliminar_pedido_compra, name='eliminar_pedido_compra'),
]
