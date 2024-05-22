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
        return str(self.id_producto)+" "+str(self.nombre)