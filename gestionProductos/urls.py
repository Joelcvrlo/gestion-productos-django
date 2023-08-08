from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('edicionProducto/<id_producto>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<id_producto>', views.eliminarProducto),
]
