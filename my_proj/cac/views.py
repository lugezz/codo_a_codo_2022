from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    if (request.method == 'GET'):
        titulo = 'Titulo cuando se accede por GET'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'

    listado_cursos = [
        {
            'nombre': 'Fullstack Java',
            'descripcion': 'Curso de Fullstack',
            'categoria': 'Programación'
        },
        {
            'nombre': 'Diseño UX/IU',
            'descripcion': '🎨',
            'categoria': 'Diseño'
        },
        {
            'nombre': 'Big Data',
            'descripcion': 'test',
            'categoria': 'Analisis de Datos'
        },
    ]

    parameters_get = request.GET.get('param')
    print(parameters_get)

    context = {
        'titulo': titulo,
        'cursos': listado_cursos,
        'parametros': parameters_get,
    }

    return render(request, 'cac/index.html', context)


# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')


def saludar(request, nombre=''):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
    """)


# def ver_proyectos(request, anio, mes):
#     return HttpResponse(f"""
#         <h1>Proyectos del  - {mes}/{anio}</h1>
#         <p>Listado de proyectos</p>
#     """)
def ver_proyectos(request, anio=2022, mes=1):
    proyectos = []
    return render(request, 'cac/proyectos.html', {'proyectos': proyectos})


def ver_cursos(request):
    listado_cursos = [
        {
            'nombre': 'Fullstack Java',
            'descripcion': 'Curso de Fullstack',
            'categoria': 'Programación'
        },
        {
            'nombre': 'Diseño UX/IU',
            'descripcion': '🎨',
            'categoria': 'Diseño'
        },
        {
            'nombre': 'Big Data',
            'descripcion': 'test',
            'categoria': 'Analisis de Datos'
        },
    ]

    return render(request, 'cac/cursos.html', {'cursos': listado_cursos})


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
    # return redirect('saludar_por_defecto')
    # return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('cac/quienes_somos.html')
    context = {'titulo': 'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context, request))
