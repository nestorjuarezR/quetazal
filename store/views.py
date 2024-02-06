from django.shortcuts import render, get_object_or_404
from .models import Categoria, Articulo
from taggit.models import Tag
from django.db.models import Count


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

    #Lista de articulos similares
    articulos_tags_all = articulo.tags.values_list('id', flat=True)
    articulos_similares = Articulo.disponibles.filter(
                                                                                            tags__in=articulos_tags_all).exclude(id=articulo.id)
    articulos_similares = articulos_similares.annotate(same_tags = Count('tags')).order_by('-same_tags', '-titulo')[:3]

    return render(request, 
                                'store/articulo.html',
                                {'articulo': articulo,
                                 'articulos_similares': articulos_similares})



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



def custom_404_view(request, exception):
    return render(request, 'store/404.html', status=404)

def custom_500_view(request):
    return render('store/500.html', status=500)

def robots(request):
    return render(request, 
                  'store/txt/robots.txt', 
                  content_type='text/plain',
                  context={'domain_url': "https://www.tudiamastriste.com"})


def security(request):
    return render(request,
                  'store/txt/security.txt',
                  content_type="text/plain")
