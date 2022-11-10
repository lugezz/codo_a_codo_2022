from django.urls import path, re_path

from cac.views import (
    CategoriaView, categorias_editar, categorias_eliminar,
    cursos, cursos_detalle, hola_mundo,
    index, index_administracion, quienes_somos,
    saludar, ver_cursos, ver_proyectos)

urlpatterns = [
    path('', index, name='inicio'),
    path('quienessomos/', quienes_somos, name='quienes_somos'),
    path('cursos/', ver_cursos, name='cursos'),
    path('administracion', index_administracion, name='inicio_administracion'),

    path('administracion/categorias/nuevo', CategoriaView.as_view(), name='categorias_nuevo'),
    path('administracion/categorias/editar/<int:id_categoria>', categorias_editar, name='categorias_editar'),
    path('administracion/categorias/eliminar/<int:id_categoria>', categorias_eliminar, name='categorias_eliminar'),

    path('hola_mundo/', hola_mundo),
    path('proyectos/', ver_proyectos, name='proyectos'),
    path('saludar/', saludar, name='saludillo-por-defecto'),
    path('saludar/<str:nombre>', saludar, name='saludillo-por-nombre'),
    # path('proyectos/2022/07', ver_proyectos_2022_07),
    # re_path(r'^proyectos/(?P<anio>\d{2,4})/$', ver_proyectos_anio),
    # path('proyectos/<int:anio>/<int:mes>', ver_proyectos, name="ver_proyectos"),
    path('cursos/detalle/<slug:nombre_curso>', cursos_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$', cursos, name="cursos"),
]
