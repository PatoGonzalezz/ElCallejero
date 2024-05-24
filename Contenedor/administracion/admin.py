from django.contrib import admin
from .models import Producto, Estado, Pedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Estado)
admin.site.register(Pedido)   