from django.shortcuts import render
from administracion.models import Pedido, Estado
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.

def lista_pedidos(request):
    busqueda = request.GET.get("buscar")
    lista_pedidos = Pedido.objects.raw("SELECT * FROM administracion_Pedido")

    if busqueda:
        lista_pedidos = Pedido.objects.filter( 
            Q(id_pedido__icontains = busqueda)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator (lista_pedidos, 10)
        lista_pedidos = paginator.page(page)
    except:
        raise Http404
    context = {"pedidos":lista_pedidos}
    return render(request,'pedidos.html',context)