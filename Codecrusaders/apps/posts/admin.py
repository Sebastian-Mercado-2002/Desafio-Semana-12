from django.contrib import admin
from .models import Categoria, Etiqueta, Articulo


# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'creacion', 'actualizacion')

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'creacion', 'actualizacion')

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'categoria', 'autor', 'creacion', 'actualizacion')


