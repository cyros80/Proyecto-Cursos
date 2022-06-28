from django.contrib import admin
from .models import Cursos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('id', 'fechaCreacion', 'updated') 

admin.site.register(Cursos, AdministrarModelo)