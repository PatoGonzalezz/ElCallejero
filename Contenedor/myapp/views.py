from django.shortcuts import render
from django.http import HttpResponse
import mercadopago
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def template(request):
    return render (request, 'template.html')

def carrito(request):
    return render(request, 'carrito.html', {
        'public_key': settings.MERCADO_PAGO_PUBLIC_KEY
    })

def pago_exitoso(request):
    return render(request, 'success.html')

def pago_fallido(request):
    return render(request, 'failure.html')

def pago_pendiente(request):
    return render(request, 'pending.html')


def login(request):
    return render (request, 'login.html')

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