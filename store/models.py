from django.db import models
from django.urls import reverse

#Custom Model Manager.
class CategoriaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Categoria.Status.ACTIVA)



#Modelo Categoria
class Categoria(models.Model):
     
    class Status(models.TextChoices):
        DESACTIVADA = 'DT', 'Desactivada'
        ACTIVA = 'AT', 'Activa'

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length=2,
                                                choices = Status.choices,
                                                default = Status.ACTIVA)
    
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
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descripcion = models.CharField(max_length=240)
    precio = models.IntegerField()

    class Meta:
        ordering = ['-titulo']

    def __str__(self):
        return self.titulo
