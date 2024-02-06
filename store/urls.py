from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<slug:categoria_nombre>/', views.articulos_categoria, name='articulos_categoria'),
    path('articulo/<int:id>/<slug:slug>/', views.articulo, name='articulo_detalle'),
    path('tag/<slug:tag_slug>/', views.tag_listado, name="tag_listado"),

    path('robots.txt/', views.robots, name='robots'),
    path('security.txt/', views.security, name='security')
]