from ast import Return
from urllib import request
from django.shortcuts import render

from contenido.views import cursos
from .models import Cursos

# Create your views here.

def curso(request):
    cursos=Cursos.objects.all()


    return render(request,"cursos/principal.html",{'cursos':cursos})    