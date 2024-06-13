from django.shortcuts import render, redirect
from django.http import HttpResponse
from administracion.models import Producto, Pedido, Estado
from myapp.carrito import Carrito
from django.contrib import messages
import mercadopago
from django.conf import settings
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponseRedirect
import requests



# Create your views here.

def index(request):
    productos = Producto.objects.all()
    ciudad = 'Coquimbo,CL'
    temperatura, descripcion_clima, humedad = obtener_clima(ciudad)
    return render(request, "index.html", {'productos': productos, 'temperatura': temperatura, 'descripcion_clima': descripcion_clima, 'humedad': humedad})

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

def crear_preferencia_pago(descripcion, precio_total):
    sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
    
    preference_data = {
        "items": [
            {
                "title": descripcion,
                "quantity": 1,
                "currency_id": "CLP",  # O la moneda que uses
                "unit_price": float(precio_total)  # Asegúrate de convertir a float
            }
        ],
        "back_urls": {
            "success": 'success',
            "failure": "https://www.tusitio.com/failure",
            "pending": "https://www.tusitio.com/pending"
        },
        "auto_return": "approved",
    }
    
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return preference['init_point']

def agregar_pedido(request):
    if request.method == "POST":
        descripcion  = request.POST.get("descripcion")
        precio_total = request.POST.get("precio_total")

        try:
            # Crear y guardar el pedido
            objProducto = Pedido.objects.create(
                id_estado=Estado.objects.get(id_estado=3),
                descripcion=descripcion,
                precio_total=precio_total
            )
            objProducto.save()

            # Crear la preferencia de pago
            init_point = crear_preferencia_pago(descripcion, precio_total)

            # Redirigir al usuario a la URL de Mercado Pago
            return HttpResponseRedirect(init_point)
        except Exception as e:
            messages.error(request, f"Error al realizar el pedido y procesar el pago: {e}")
            return redirect('carrito')
    else:
        messages.error(request, "Método no permitido")
        return redirect('carrito')
    
def obtener_clima(ciudad):
    clave_api = 'b0a2dc695c39fc385ff089860e1a4e93'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}&units=metric'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error al hacer la solicitud
        datos_clima = response.json()
        temperatura = datos_clima['main']['temp']
        descripcion_clima = datos_clima['weather'][0]['description']
        humedad = datos_clima['main']['humidity']
        return temperatura, descripcion_clima, humedad
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud a la API:", e)
        return None, None, None