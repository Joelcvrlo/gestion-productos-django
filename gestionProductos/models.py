from django.db import models


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)
    descripcion_categoria = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nombre_categoria)
        # return texto.format(self.nombre_categoria)


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.nombre_proveedor)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_stock = models.IntegerField()
    fecha_ingreso = models.DateField()
    def __str__(self):
        return '%s' % (self.nombre_producto)

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=40)
    numero_telefono = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.nombre)

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    tipo_transaccion = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    fecha_factura = models.DateField()
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.id_factura)

class DetalleFactura(models.Model):
    id_detfac = models.IntegerField(primary_key=True)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    def __str__(self):
        return '%s' % (self.id_detfac)