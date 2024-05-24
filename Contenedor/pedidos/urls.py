from django.urls import path
from . import views

urlpatterns=[
    path('pedidos', views.lista_pedidos, name='lista_pedidos'),
]