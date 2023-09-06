from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('productos/', views.productos, name="productos"),
    path('carrito/', views.carrito, name="carrito" ),
    path('formulario/', views.prodFormulario, name="prodFormulario")
]