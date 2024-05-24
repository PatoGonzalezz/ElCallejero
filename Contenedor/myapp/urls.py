from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('carrito', views.carrito, name="carrito"),
    path('crear-preferencia/', views.crear_preferencia_pago, name='crear_preferencia_pago'),
    path('success/', views.pago_exitoso, name='pago_exitoso'),
    path('failure/', views.pago_fallido, name='pago_fallido'),
    path('pending/', views.pago_pendiente, name='pago_pendiente'),
    path('agregar/<str:pk>/', views.agregar_producto, name="Add"),
    path('eliminar/<str:pk>/', views.eliminar_producto, name="Del"),
    path('restar/<str:pk>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('pedido/', views.agregar_pedido, name="AddPedido"),

]
