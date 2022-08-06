from ast import Return
from urllib import request
from django.shortcuts import render
from .forms import ComentarioCursoForm
from django.shortcuts import get_object_or_404
import datetime

from contenido.views import cursos
from .models import ComentarioCurso, Cursos

# Create your views here.

def curso(request):
    cursos=Cursos.objects.all()


    return render(request,"cursos/principal.html",{'cursos':cursos})   

def comentario(request):
    comentarios=ComentarioCurso.objects.all()


    return render(request,"cursos/comentarioVista.html",{'comentarios':comentarios}) 

def registrar(request):
    if request.method=='POST':
        form = ComentarioCursoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComentarioCurso.objects.all()
            return render (request,"cursos/comentarioVista.html",
            {'comentarios':comentarios})
    form = ComentarioCursoForm()
    return render (request,'cursos,contacto.html',{'form': form})

def contacto(request):
    return render(request,"cursos/contacto.html")

    
def eliminarComentarioContacto(request, id,
      confirmacion='cursos/confirmarEliminacion.html'):
      comentario = get_object_or_404(ComentarioCurso, id=id)
      if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioCurso.objects.all()
        return render(request,"cursos/comentarioVista.html",
            {'comentarios':comentarios})
      return render(request, confirmacion, {'object':comentario}) 

def consultarComentarioIndividual(request, id):
    comentario=ComentarioCurso.objects.get(id=id)
#get permite establecer una condicionante a la consulta y recupera el objetos
#del modelo que cumple la condición (registro de la tabla ComentariosContacto.
#get se emplea cuando se sabe que solo hay un objeto que coincide con su
#consulta.
    return render(request,"cursos/formEditarComentario.html",
            {'comentario':comentario})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados.
                          

def editarComentarioContacto(request, id):
      comentario = get_object_or_404(ComentarioCurso, id=id)
      form = ComentarioCursoForm(request.POST, instance=comentario)
#Referenciamos que el elemento del formulario pertenece al comentario
# ya existente
      if form.is_valid():
            form.save() #si el registro ya existe, se modifica.
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/comentarioVista.html",
                    {'comentarios':comentarios})
#Si el formulario no es valido nos regresa al formulario para verificar
#datos
      return render(request,"cursos/formEditarComentario.html",
      {'comentario':comentario})   

def consultar1(request):
#con una sola condición
    cursos=Cursos.objects.filter(id="1")
    return render(request,"cursos/consultas.html",{'cursos':cursos})


def consultar2(request):
#multiples condiciones adicionando .filter() se analiza
#como AND
    cursos=Cursos.objects.filter(nombre="Manejo de Bases de Datos MySql").filter(capitulos
    =8)
    return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar3(request):
#Si solo deseamos recuperar ciertos datos agregamos la
#función only, listando los campos que queremos obtener de
#la consulta emplear filter() o #en el ejemplo all()
    cursos=Cursos.objects.all().only("nombre", "profesor",
    "categoria", "capitulos", "imagen")
    return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar4(request):
    cursos=Cursos.objects.filter(categoria__contains="Java")
    return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar5(request):
    cursos=Cursos.objects.filter(id__in=[1, 4])
    return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar6(request):
    fechaInicio = datetime.date(2022, 6, 28)
    fechaFin = datetime.date(2022, 6, 30)
    cursos=Cursos.objects.filter(fechaCreacion__range=(fechaInicio,fechaFin))
    return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar7(request):
#Consultando entre modelos
    cursos=Cursos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"cursos/consultas.html",{'cursos':cursos})   

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"cursos/seguridad.html",
    {'nombre':nombre})
