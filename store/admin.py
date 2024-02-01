from django.contrib import admin
from .models import Categoria, Articulo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status']
    list_filter = ['status']
    prepopulated_fields = {'slug' : ('titulo' ,)}
    ordering = ['titulo', 'status']

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio']
    list_filter = ['titulo']
    prepopulated_fields = {'slug' : ('titulo' ,)}
    ordering = ['titulo', 'precio']