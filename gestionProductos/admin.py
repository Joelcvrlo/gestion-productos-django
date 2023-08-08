from django.contrib import admin
from gestionProductos.models import Categoria, Proveedor, Producto, Cliente, Factura, DetalleFactura

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)