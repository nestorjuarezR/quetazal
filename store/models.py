from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager



#Custom Model Manager.
class CategoriaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Categoria.Status.ACTIVA)


class ArticuloManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(disponible=True)



#Modelo Categoria
class Categoria(models.Model):
     
    class Status(models.TextChoices):
        DESACTIVADA = 'DT', 'Desactivada'
        ACTIVA = 'AT', 'Activa'

    titulo = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, blank=False)
    status = models.CharField(max_length=2,
                                                choices = Status.choices,
                                                default = Status.ACTIVA)
    imagen = models.ImageField(upload_to='categorias',
                                                            blank=False)
    creacion = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()   #Manager por defecto
    activas = CategoriaManager() #Custom manager

    class Meta:
        ordering = ['-titulo']

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('articulos_categoria',
                       args=[str(self.slug)])


        

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria,
                                                                    on_delete = models.CASCADE,
                                                                    related_name = 'categoria')
    titulo = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, blank=False)
    descripcion = models.CharField(max_length=240, blank=False)
    precio = models.IntegerField(blank=False)
    sku = models.CharField(max_length=50, unique=True, blank=False)  # Añadir esta línea para el SKU
    imagen = models.ImageField(upload_to='articulos',
                                                            default='articulos/articulo.jpg',
                                                            blank=False)
    tags = TaggableManager(blank=False)
    disponible = models.BooleanField(default=True, blank=False)
    creacion = models.DateTimeField(auto_now_add=True, blank=False)


    class Meta:
        ordering = ['-titulo']

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('articulo_detalle',
                       args=[self.id,
                                    self.slug])
    
    objects = models.Manager()   #Manager por defecto
    disponibles = ArticuloManager() #Custom manager

