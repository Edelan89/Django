from django.shortcuts import render
from .models import Productos

# Create your views here.

def tienda(request):

    productos = Productos.objects.all()

    return render(request, "tienda/tienda.html", {"productos" : productos})