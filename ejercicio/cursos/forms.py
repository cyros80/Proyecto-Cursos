from dataclasses import fields
from django import forms

from cursos.models import ComentarioCurso



class ComentarioCursoForm(forms.ModelForm):
    class Meta:
        model= ComentarioCurso
        fields= ['usuario','mensaje']