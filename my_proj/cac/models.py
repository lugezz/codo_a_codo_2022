from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(max_length=150)
    dni = models.IntegerField(verbose_name="DNI")
