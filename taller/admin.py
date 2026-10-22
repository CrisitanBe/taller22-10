from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "nacionalidad")
    search_fields = ("nombre", "nacionalidad")

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "fecha_publicacion")
    list_filter = ("fecha_publicacion", "autor")
    search_fields = ("titulo",)
    autocomplete_fields = ("autor",) 