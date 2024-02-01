from django.shortcuts import render, get_object_or_404
from .models import Categoria, Articulo

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def categorias(request):

    categoria = Categoria.activas.all()
    return render(request, 
                  'store/categorias.html',
                  {'categorias': categoria})

def articulos_categoria(request, categoria_nombre):
    categoria = get_object_or_404(Categoria, slug=categoria_nombre)
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 
                                'store/articulos_listado.html',
                                {'articulos': articulos,
                                 'categoria': categoria})