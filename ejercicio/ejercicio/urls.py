"""ejercicio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from contenido import views
from django.conf import settings
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_cursos.curso, name="Principal"),
    path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views_cursos.contacto, name="Contacto"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('prueba/', views.prueba, name="Prueba"),
    path('registrar/', views_cursos.registrar, name="Registrar"),
    path('comentarios/',views_cursos.comentario, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_cursos.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_cursos.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_cursos.editarComentarioContacto, name='Editar'),
    path('consultas1',views_cursos.consultar1, name="Consultas"),
    path('consultas2',views_cursos.consultar2, name="Consultas2"),
    path('consultas3',views_cursos.consultar3, name="Consultas3"),
    path('consultas4',views_cursos.consultar4, name="Consultas4"),
    path('consultas5',views_cursos.consultar5, name="Consultas5"),
    path('consultas6',views_cursos.consultar6, name="Consultas6"),
    path('consultas7',views_cursos.consultar7, name="Consultas7"),
    path('seguridad',views_cursos.seguridad, name="Seguridad"),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)

