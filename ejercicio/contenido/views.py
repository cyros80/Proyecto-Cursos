from django.shortcuts import render, HttpResponse

# Create your views here.

menu="""
    <a href="/">Home</a>
    <a href="/cursos">Cursos Disponibles</a>
    <a href="/contacto">Contactanos</a>
"""    


def principal(request):
    contenido="""<h1>Hola Bienvenido </h1>
    <p>Descrpcion del sitio web</p>"""
    return HttpResponse(menu + contenido)

def cursos(request):
    contenido="""<h1>Cursos Disponibles</h1>
    <table class="default">
    <tr>
    <td>Word</td>
    </tr>
    <tr>
    <td>Excel</td>
    </tr>
     <tr>
    <td>Python</td>
    </tr>
    </table>"""
    return HttpResponse(menu+contenido)    

def contacto(request):
    contenido="""<h1>Contactos </h1>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Correo:<input type="text" name="correo"></p>
    <p>Cursos:</p>
    <select name=cursos>
    <option>Word</option>
    <option>Excel</option>
    <option>Python</option>
    </select>   
    <p>Comentarios:</p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="button" name="enviar" value="Enviar"/></p>"""
    return HttpResponse(menu+contenido)