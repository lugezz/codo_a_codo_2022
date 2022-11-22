from django.db import models
from django.utils.text import slugify


# class Persona(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     apellido = models.CharField(max_length=150, verbose_name='Apellido')
#     email = models.EmailField(max_length=150, null=True)
#     dni = models.IntegerField(verbose_name="DNI")

#     def get_full_name(self):
#         return f'{self.apellido}, {self.nombre}'

#     def __str__(self) -> str:
#         return self.get_full_name()


# class Estudiante(models.Model):
#     persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
#     matricula = models.CharField(max_length=10, verbose_name='Matricula')

#     def __str__(self) -> str:
#         return f'{self.persona.get_full_name()} - {self.matricula}'

class PersonaM(models.Model):
    nombre_m = models.CharField(max_length=100, verbose_name='Nombre')
    apellido_m = models.CharField(max_length=150, verbose_name='Apellido')
    email_m = models.EmailField(max_length=150, null=True)
    dni_m = models.IntegerField(verbose_name="DNI")


class EstudianteM(PersonaM):
    matricula_m = models.CharField(max_length=10, verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.nombre_m} {self.apellido_m} ({self.matricula_m})"

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.nombre


# class Curso(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     descripcion = models.TextField(null=True, verbose_name='Descripcion')
#     fecha_inicio = models.DateField(verbose_name='Fecha de inicio', null=True, default=None)
#     portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Portada')
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relacion mucho a uno
#     estudiantes = models.ManyToManyField(EstudianteM, through='Inscripcion')  # Related_name="cursos"

#     def __str__(self):
#         return self.nombre

#     def delete(self, using=None, keep_parents=False):
#         self.portada.storage.delete(self.portada.name)  # Borrado fisico
#         super().delete()


# class Curso(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     descripcion = models.TextField(null=True, verbose_name='Descripcion')
#     # fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
#     # portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#     # Many to many puede estar en cualquiera de las 2, pero no en las 2
#     # estudiantes = models.ManyToManyField(Estudiante) Lo saco de aquí si se define en trabajar
#     # con otro modelo si quiero agregar otro campo como nota
#     estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion')

#     def __str__(self) -> str:
#         return self.nombre


# herencia clase abstracta
# class PersonaAbs(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     apellido = models.CharField(max_length=150, verbose_name='Apellido')
#     email = models.EmailField(max_length=150, null=True)
#     dni = models.IntegerField(verbose_name="DNI")

#     class Meta:
#         abstract = True


# class EstudianteAbs(PersonaAbs):
#     matricula = models.CharField(max_length=10, verbose_name='Matricula')


# class DocenteAbs(PersonaAbs):
#     legajo = models.CharField(max_length=10, verbose_name='Legajo')


class CursoM(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio', null=True, default=None)
    portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Portada')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relacion mucho a uno
    estudiantes = models.ManyToManyField(EstudianteM)  # Related_name="cursos"

    def __str__(self):
        return self.nombre

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)  # Borrado fisico
        super().delete()


# HERENCIA MULTIPLE
class Inscripcion(models.Model):

    ESTADOS = [
        (1, 'Inscripto'),
        (2, 'Cursando'),
        (3, 'Egresado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(EstudianteM, on_delete=models.CASCADE)
    curso = models.ForeignKey(CursoM, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS, default=1)

    def __str__(self):
        return f'{self.id} - {self.estudiante} - {self.curso}'

    class Meta:
        verbose_name_plural = "Inscripciones"


class DocenteM(PersonaM):
    legajo_m = models.CharField(max_length=10, verbose_name='Legajo')


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100, verbose_name='Nombre Slug')
    anio = models.IntegerField(verbose_name='Año')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    url = models.URLField(max_length=100, verbose_name='Url')
    portada = models.ImageField(upload_to='imagenes/proyecto/', null=True, verbose_name='Portada')
    estudiante = models.ForeignKey(EstudianteM, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    """ Sobreescribo el metodo save del modelo"""
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)  # Borrado fisico
        super().delete()
