from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
import os

from .models import Categoria, Articulo

@receiver(pre_delete, sender=Categoria)
def eliminar_imagen_categoria(sender, instance, **kwargs):
    # Eliminar la imagen asociada a la categoría cuando la categoría se elimina
    if instance.imagen:
        # Obtener la ruta completa del archivo
        ruta_archivo = instance.imagen.path

        # Eliminar el archivo si existe
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

@receiver(pre_delete, sender=Articulo)
def eliminar_imagenes_articulo(sender, instance, **kwargs):
    # Eliminar la imagen principal del artículo
    if instance.imagen:
        ruta_archivo = instance.imagen.path
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

    # Eliminar todas las imágenes adicionales asociadas al artículo
    for imagen_producto in instance.imagenes.all():
        if imagen_producto.imagen:
            ruta_archivo = imagen_producto.imagen.path
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)


