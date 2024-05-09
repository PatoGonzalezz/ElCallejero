from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('carrito', views.carrito, name="carrito"),
    path('login', views.login, name="login")
]
