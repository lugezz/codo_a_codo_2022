from django.urls import path

from cac.views import hola_mundo, saludar

urlpatterns = [
    path('hola_mundo/', hola_mundo),
    path('saludar/', saludar, name='saludillo-por-defecto'),
    path('saludar/<str:nombre>', saludar, name='saludillo-por-nombre'),
]
