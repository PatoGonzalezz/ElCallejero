from django.shortcuts import render, redirect
from administracion.models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from administracion.forms import ProductoForm
from .models import Producto

# Create your views here.
def register(request):
    return render(request,"registration/register.html")

@login_required
def menu (request):
    request.session["usuario"]="pato"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, "admin_index.html",context)

@login_required
def inicio (request):
    lista_productos = Producto.objects.all()
    context={"productos":lista_productos}
    return  render(request,'admin_index.html', context)


def lista_productos(request):
    busqueda = request.GET.get("buscar")
    lista_productos = Producto.objects.raw("SELECT * FROM administracion_Producto")

    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) | 
            Q(id_producto__icontains = busqueda)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator (lista_productos, 5)
        lista_productos = paginator.page(page)
    except:
        raise Http404
    context = {"productos":lista_productos}
    return render(request,'admin_index.html',context)


def agregar_productos(request):
    if request.method == "POST":
        nombre_prod = request.POST.get("nombre")
        desc = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        precio_prod = request.POST.get("precio")
        stock_prod = request.POST.get("stock")

        if not nombre_prod or not desc or not imagen or not precio_prod or not stock_prod:
            messages.error(request, "Todos los campos son requeridos.")
            return render(request, 'add_prod.html')

        try:
            objProducto = Producto.objects.create(
                nombre=nombre_prod,
                descripcion=desc,
                foto_producto=imagen,
                precio=precio_prod,
                stock=stock_prod
            )
            objProducto.save()
            messages.success(request, "Producto Agregado")
            return redirect('admin_index')  # Ajusta esto según tu URL

        except Exception as e:
            messages.error(request, f"Error al agregar el producto: {e}")
            return render(request, 'add_prod.html')

    return render(request, 'add_prod.html')

def eliminar_productos(request,pk):
    
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete() #delete en la BD
        messages.success(request,"Producto Eliminado")
        lista_producto = Producto.objects.all()
        context={"productos":lista_producto}
        return render(request,'admin_index.html',context)
    except:
        lista_producto = Producto.objects.all()
        context={"productos":lista_producto}
        return render(request,'admin_index.html',context)
    
def actualizar_productos(request):
    
    if request.method == "POST":
        #rescatamos en variables los valores del formulario (name)
        id_prod         = request.POST["id"]
        nombre_prod     = request.POST["nombre"]
        descripcion     = request.POST["descripcion"]
        imagen          = request.FILES["imagen"]
        precio_prod     = request.POST["precio"]
        stock_prod      = request.POST["stock"]

        #crea Producto (izd: nombre del campo de la BD, derecho: variable local)
        objProducto = Producto()
        objProducto.id_producto   = id_prod
        objProducto.nombre        = nombre_prod
        objProducto.descripcion   = descripcion
        objProducto.foto_producto = imagen
        objProducto.precio        = precio_prod
        objProducto.stock         = stock_prod
        
        objProducto.save() #update en la base de datos
        messages.success(request, "Producto Actualizado")
        lista_Producto = Producto.objects.all()
        context = {"productos":lista_Producto}
        return render(request,'admin_index.html',context)
    else:
        lista_Producto = Producto.objects.all()
        context = {"productos":lista_Producto}
        return render(request,'edit_prod.html',context)
    

def buscar_productos(request,pk):
    if pk != 0:
        producto = Producto.objects.get(id_producto=pk)
        context={"producto":producto}
        if producto:
            return render(request,'edit_prod.html', context)
        else:
            context = {"mensaje":"El producto no existe"}
            return render(request,'admin_index.html',context) 