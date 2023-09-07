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


]