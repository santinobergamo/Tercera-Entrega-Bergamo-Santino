from django.contrib import admin
from .models import Producto, Proveedor, PedidoCompra

# Configuración personalizada para el modelo Producto
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']
    search_fields = ['nombre', 'codigo']
    list_filter = ['nombre']

# Registra el modelo Producto con la configuración personalizada
admin.site.register(Producto, ProductosAdmin)

# Registra el modelo Proveedor
admin.site.register(Proveedor)

# Registra el modelo PedidoCompra
admin.site.register(PedidoCompra)
