from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    if (request.method == 'GET'):
        titulo = 'Titulo cuando se accede por GET'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    return HttpResponse(f"""
        <h1>{titulo}</h1>
        <p></p>
    """)


# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')


def saludar(request, nombre=''):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
    """)


def ver_proyectos(request, anio, mes):
    return HttpResponse(f"""
        <h1>Proyectos del  - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)


def cursos(request, nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)


def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def ver_proyectos_anio(request, anio):
    return HttpResponse(f"""
        <h1>Proyectos del  {anio}</h1>
        <p>Listado de proyectos</p>
    """)


def ver_proyectos_2022_07(request):
    return HttpResponse("""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de proyectos</p>
    """)


def quienes_somos(request):
    # return redirect('saludillo-por-defecto')
    return redirect(reverse('saludillo-por-nombre', kwargs={'nombre': 'Cachula'}))
