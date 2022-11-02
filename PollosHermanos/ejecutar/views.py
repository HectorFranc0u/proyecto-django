from django.shortcuts import render
from .models import tbProductos, tbProveedores,  tbSucursales, tbCombos

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("<h1></h1>")