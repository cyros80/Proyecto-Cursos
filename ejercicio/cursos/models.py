
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

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
        
