from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('productos/', views.productos, name="productos"),
    path('carrito/', views.carrito, name="carrito" ),
    path('formulario', views.prodFormulario, name="prodFormulario"),
    path('buscarProducto', views.buscar, name="buscarProducto"),
    path('resultadoBusqueda/', views.busquedaProducto, name="resultadoBusqueda" ),
    path('mostrarFormularioBusqueda/', views.mostrar_formulario_busqueda, name='mostrarFormularioBusqueda'),
    path('editarProducto/<int:id>/', views.editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name="eliminarProducto"),
    path('crear_pedido_compra/', views.crear_pedido_compra, name='crear_pedido_compra'),
    path('lista_pedidos_compra/', views.lista_pedidos_compra, name='lista_pedidos_compra'),


]