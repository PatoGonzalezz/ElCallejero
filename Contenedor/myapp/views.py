from django.shortcuts import render, redirect
from django.http import HttpResponse
from administracion.models import Producto
from myapp.carrito import Carrito
import mercadopago
from django.conf import settings
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    return render(request, "index.html", {'productos':productos})

def template(request):
    return render (request, 'template.html')

def carrito(request):
    return render(request, 'carrito.html', {
        'public_key': settings.MERCADO_PAGO_PUBLIC_KEY
    })
    
def agregar_producto(request, pk):    
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")    

def pago_exitoso(request):
    return render(request, 'success.html')

def pago_fallido(request):
    return render(request, 'failure.html')

def pago_pendiente(request):
    return render(request, 'pending.html')

def crear_preferencia_pago(request):
    sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
    
    preference_data = {
        "items": [
            {
                "title": "Nombre del producto",
                "quantity": 1,
                "currency_id": "CLP",  # O la moneda que uses
                "unit_price": 10000.0  # Precio del producto
            }
        ],
        "back_urls": {
            "success": "https://www.tusitio.com/success",
            "failure": "https://www.tusitio.com/failure",
            "pending": "https://www.tusitio.com/pending"
        },
        "auto_return": "approved",
    }
    
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return JsonResponse({
        'init_point': preference['init_point'],
        'preference_id': preference['id']
    })

