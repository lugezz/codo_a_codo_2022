from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings


from cac.views import (
    CategoriaListView, api_proyectos, hola_mundo,
    categorias_editar, categorias_eliminar,
    cursos, cursos_detalle,
    cursos_editar, cursos_eliminar, cursos_index, cursos_nuevo,
    estudiantes_editar, estudiantes_eliminar, estudiantes_index, estudiantes_nuevo,
    proyectos_editar, proyectos_eliminar, proyectos_index, proyectos_nuevo,
    index, index_administracion, quienes_somos,
    saludar, ver_cursos)

urlpatterns = [
    path('', index, name='inicio'),
    path('quienessomos/', quienes_somos, name='quienes_somos'),
    path('cursos/', ver_cursos, name='cursos'),
    path('administracion', index_administracion, name='inicio_administracion'),
    path('api_proyectos/', api_proyectos, name="api_proyectos"),

    path('administracion/', index_administracion, name='inicio_administracion'),

    path('administracion/categorias', CategoriaListView.as_view(), name='categorias_index'),

    path('administracion/categorias/editar/<int:id_categoria>', categorias_editar, name='categorias_editar'),
    path('administracion/categorias/eliminar/<int:id_categoria>', categorias_eliminar, name='categorias_eliminar'),

    path('administracion/cursos', cursos_index, name='cursos_index'),
    path('administracion/cursos/nuevo/', cursos_nuevo, name='cursos_nuevo'),
    path('administracion/cursos/editar/<int:id_curso>', cursos_editar, name='cursos_editar'),
    path('administracion/cursos/eliminar/<int:id_curso>', cursos_eliminar, name='cursos_eliminar'),

    path('administracion/estudiantes', estudiantes_index, name='estudiantes_index'),
    path('administracion/estudiantes/nuevo/', estudiantes_nuevo, name='estudiantes_nuevo'),
    path('administracion/estudiantes/editar/<int:id_estudiante>', estudiantes_editar, name='estudiantes_editar'),
    path('administracion/estudiantes/eliminar/<int:id_estudiante>', estudiantes_eliminar, name='estudiantes_eliminar'),

    path('administracion/proyectos', proyectos_index, name='proyectos_index'),
    path('administracion/proyectos/nuevo/', proyectos_nuevo, name='proyectos_nuevo'),
    path('administracion/proyectos/editar/<int:id_proyecto>', proyectos_editar, name='proyectos_editar'),
    path('administracion/proyectos/eliminar/<int:id_proyecto>', proyectos_eliminar, name='proyectos_eliminar'),

    path('hola_mundo/', hola_mundo),
    path('saludar/', saludar, name='saludillo-por-defecto'),
    path('saludar/<str:nombre>', saludar, name='saludillo-por-nombre'),
    # path('proyectos/2022/07', ver_proyectos_2022_07),
    # re_path(r'^proyectos/(?P<anio>\d{2,4})/$', ver_proyectos_anio),
    # path('proyectos/<int:anio>/<int:mes>', ver_proyectos, name="ver_proyectos"),
    path('cursos/detalle/<slug:nombre_curso>', cursos_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$', cursos, name="cursos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
