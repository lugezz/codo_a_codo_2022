from django.http import HttpResponse


# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')


def saludar(request, nombre=''):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
    """)
