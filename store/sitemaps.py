from django.contrib.sitemaps import Sitemap
from .models import Categoria, Articulo

class CategoriaSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Categoria.activas.all()
    
    def lastmod(self, obj):
        return obj.creacion
    
class ArticuloSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Articulo.objects.filter(disponible=True)

    def lastmod(self, obj):
        return obj.creacion