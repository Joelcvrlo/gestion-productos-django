from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('edicionProducto/<id_producto>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<id_producto>', views.eliminarProducto),
    path('eliminarCategoría/<id_categoria>', views.eliminarCategoría),
    path('eliminarProveedor/<id_proveedor>', views.eliminarProveedor),
    path('eliminarCliente/<rut_cliente>', views.eliminarCliente),
    path('eliminarFactura/<id_factura>', views.eliminarFactura),
    path('eliminarDetallefactura/<id_detfac>', views.eliminarDetallefactura),
]
