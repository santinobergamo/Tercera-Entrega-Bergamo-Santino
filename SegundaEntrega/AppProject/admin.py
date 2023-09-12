from django.contrib import admin
from .models import *
from datetime import datetime

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']
    search_fields = ['nombre', 'codigo']
    list_filter = ['nombre']


# Register your models here.
admin.site.register(Producto, ProductosAdmin)
