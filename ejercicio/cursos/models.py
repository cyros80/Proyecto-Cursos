
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model):
    id =models.BigAutoField(primary_key=True,verbose_name="No. Identificacion")
    nombre = models.TextField(max_length=100, verbose_name="Curso")
    profesor =models.TextField(max_length=70,verbose_name="Maestro del Curso")
    categoria=models.TextField(max_length=30,verbose_name="Tema")
    capitulos= models.IntegerField(verbose_name="Secciones")
    imagen = models.ImageField(null=True, upload_to ="fotos", verbose_name="Fotografia")
    fechaCreacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha en que se creo")
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecho en que se Actualizo")

    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["fechaCreacion"]

    def __str__(self):
        return self.nombre    
        
class CursoComentario(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="Identificador")
    profesor = models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Curso En El Que Desea Comentar")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Alta")
    comentario = RichTextField(verbose_name="Comentario")     

    
    class Meta:
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return self.comentario

class ComentarioCurso(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Curso"
        verbose_name_plural = "Comentarios Cursos"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje
#Indica que se mostrára el mensaje como valor en la tabla        

    
