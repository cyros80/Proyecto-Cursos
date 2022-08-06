from django.contrib import admin
from .models import Cursos
from .models import CursoComentario
from .models import ComentarioCurso

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('id', 'fechaCreacion', 'updated') 
    list_display = ('nombre','id','profesor','categoria','fechaCreacion')
    search_fields = ('id','nombre','profesor','categoria')
    date_hierarchy = 'fechaCreacion'
    list_filter = ('profesor','categoria')
    list_per_page=2
    list_display_links=('id','profesor','nombre')
    list_editable=('categoria',)

    def get_readonly_fields(self, request, obj=None):
    #si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
    #Bloquea los campos
            return ('id','nombre', 'profesor')
    #Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
    #Bloquea los campos
            return ('fechaCreacion', 'updated')

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'comentario')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

class AdministrarComentariosCurso(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    
    


 

admin.site.register(CursoComentario,AdministrarComentarios)
admin.site.register(ComentarioCurso,AdministrarComentariosCurso)
admin.site.register(Cursos, AdministrarModelo)
