from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def template(request):
    return render (request, 'template.html')

def carrito(request):
    return render (request, 'carrito.html')

def login(request):
    return render (request, 'login.html')