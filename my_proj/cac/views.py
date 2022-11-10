from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import loader
from django.views import View
from django.views.generic import ListView

from cac.forms import CategoriaForm, CategoriaFormValidado, ContactoForm
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


def categorias_eliminar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'cac/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')


def categorias_nuevo(request):
    if (request.method == 'POST'):
        formulario = CategoriaFormValidado(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado()
    return render(request, 'cac/administracion/categorias/nuevo.html', {'formulario': formulario})


def categorias_editar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'cac/administracion/404_admin.html')

    if (request.method == 'POST'):
        formulario = CategoriaFormValidado(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado(instance=categoria)
    return render(request, 'cac/administracion/categorias/editar.html', {'formulario': formulario})


class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'lista_categorias'
    template_name = 'cac/administracion/categorias/index.html'
    queryset = Categoria.objects.filter(baja=False)
    ordering = ['nombre']


class CategoriaView(View):
    form_class = CategoriaForm
    template_name = 'cac/administracion/categorias/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')
        return render(request, self.template_name, {'formulario': form})
