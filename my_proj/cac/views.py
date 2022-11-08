from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import loader

from cac.forms import CategoriaForm, ContactoForm
from cac.models import Categoria


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
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)

        if contacto_form.is_valid():
            # enviar un email al administrado con los datos
            # guardar los datos en la base
            messages.success(request, 'Muchas gracias por contactarte, te esteremos respondiendo en breve.')
            messages.info(request, 'Otro mensajito')
            # deberia validar y realizar alguna accion
        else:
            messages.warning(request, 'Por favor revisa los errores')
    else:
        contacto_form = ContactoForm()

    context = {
        'titulo': titulo,
        'cursos': listado_cursos,
        'parametros': parameters_get,
        'contacto_form': contacto_form
    }

    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            pass
            # deberia validar y realizar alguna accion
    else:
        contacto_form = ContactoForm()

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


def index_administracion(request):
    variable = 'test variable'
    return render(request, 'cac/administracion/index.html', {'variable': variable})


def categorias_index(request):
    # queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request, 'cac/administracion/categorias/index.html', {'categorias': categorias})


def categorias_nuevo(request):
    if (request.method == 'POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            nueva_categoria = Categoria(nombre=nombre)
            nueva_categoria.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request, 'cac/administracion/categorias/nuevo.html', {'formulario': formulario})


def categorias_eliminar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'cac/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')
