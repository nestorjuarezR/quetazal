from django.shortcuts import render, get_object_or_404
from .models import Categoria, Articulo
from taggit.models import Tag


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

def articulo(request, id, slug):
    articulo = get_object_or_404(Articulo,
                                                                id = id,
                                                                slug = slug)
    
    return render(request, 
                                'store/articulo.html',
                                {'articulo': articulo})

def tag_listado(request, tag_slug=None):
    articulos = Articulo.disponibles.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag,
                                                        slug = tag_slug)
        articulos_list = articulos.filter(tags__in=[tag])
    
    return render(request, 
                                'store/tag_listado.html',
                                {'tag': tag,
                                 'articulos': articulos_list})

