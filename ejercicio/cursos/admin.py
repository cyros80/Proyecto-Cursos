from django.contrib import admin
from .models import Cursos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('id', 'fechaCreacion', 'updated') 
    list_display = ('nombre','id','profesor','categoria')
    search_fields = ('id','nombre','profesor','categoria')
    date_hierarchy = 'fechaCreacion'
    list_filter = ('profesor','categoria')


admin.site.register(Cursos, AdministrarModelo)