from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto     = models.AutoField  (db_column='idProducto', primary_key = True)
    foto_producto   = models.ImageField (null = True, blank = True)
    nombre          = models.CharField  (max_length=100)
    descripcion     = models.CharField  (max_length=100)
    precio          = models.IntegerField ()
    stock           = models.CharField  (max_length=100)

    def str(self):
        return str(self.nombre)+" "+str(self.precio)

class Estado(models.Model):
    id_estado     = models.AutoField(db_column='idEstado', primary_key=True)
    estado        = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.estado)

class Pedido(models.Model):
    id_pedido       = models.AutoField  (db_column='idPedido', primary_key = True)
    id_estado       = models.ForeignKey ('Estado',on_delete=models.CASCADE, db_column='idEstado', default=3) 
    descripcion     = models.CharField  (max_length=100)
    precio_total    = models.IntegerField ()

    def str(self):
        return str(self.id_pedido)+" "+str(self.descripcion)        