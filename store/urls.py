from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categorias/', views.categorias, name='categoria'),
    path('categoria/<slug:categoria_nombre>/', views.articulos_categoria, name='articulos_categoria')
]