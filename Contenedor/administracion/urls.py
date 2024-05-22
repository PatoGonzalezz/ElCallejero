from django.urls import path
from . import views

urlpatterns=[
    path('admin_index', views.lista_productos, name='lista_productos'),
    path('add_prod', views.agregar_productos, name='addProd'),
    path('deletProd/<str:pk>', views.eliminar_productos, name='delete_producto'),
    path('findProd/<str:pk>', views.buscar_productos, name='editar_ProductFind'),
    path('edit_prod', views.actualizar_productos, name="actualizar_productos"),
    path('', views.menu, name='menu'),
    path('register/', views.register, name="register" ),
]