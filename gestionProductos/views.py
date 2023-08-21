from django.shortcuts import render, redirect
from .models import Categoria, Proveedor, Producto, Cliente, Factura, DetalleFactura

# Create your views here.


def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    clientes = Cliente.objects.all()
    facturas = Factura.objects.all()
    detallefacturas = DetalleFactura.objects.all()
    return render(request, 'gestionProductos.html', {"Productos": productos, "Categorias": categorias, "Proveedores": proveedores, "Clientes": clientes, "Facturas":facturas, "Detallefacturas":detallefacturas})


def edicionProducto(request, id_producto):
    productos = Producto.objects.get(id_producto=id_producto)
    return render(request, "edicionProducto.html", {"Productos": productos})


def editarProducto(request):
    id_producto = request.POST['id_producto']
    nombre_producto = request.POST['nombre_producto']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']
    cantidad_stock = request.POST['cantidad_stock']

    producto = Producto.objects.get(id_producto=id_producto)

    producto.nombre_producto = nombre_producto
    producto.descripcion = descripcion
    producto.precio = precio
    producto.cantidad_stock = cantidad_stock
    producto.save()
    return redirect('/')

def eliminarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect('/')

def eliminarCategoría(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.delete()
    return redirect('/')

def eliminarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect('/')

def eliminarCliente(request, rut_cliente):
    cliente = Cliente.objects.get(rut_cliente=rut_cliente)
    cliente.delete()
    return redirect('/')

def eliminarFactura(request, id_factura):
    factura = Factura.objects.get(id_factura=id_factura)
    factura.delete()
    return redirect('/')

def eliminarDetallefactura(request, id_detfac):
    detallefactura = DetalleFactura.objects.get(id_detfac=id_detfac)
    detallefactura.delete()
    return redirect('/')

