from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('carrito', views.carrito, name="carrito"),
    path('login', views.login, name="login"),
    path('crear-preferencia/', views.crear_preferencia_pago, name='crear_preferencia_pago'),
    path('success/', views.pago_exitoso, name='pago_exitoso'),
    path('failure/', views.pago_fallido, name='pago_fallido'),
    path('pending/', views.pago_pendiente, name='pago_pendiente'),
]
