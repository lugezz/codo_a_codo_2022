from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(max_length=150, null=True)
    dni = models.IntegerField(verbose_name="DNI")

    def get_full_name(self):
        return f'{self.apellido}, {self.nombre}'

    def __str__(self) -> str:
        return self.get_full_name()


class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    matricula = models.CharField(max_length=10, verbose_name='Matricula')

    def __str__(self) -> str:
        return f'{self.persona.get_full_name()} - {self.matricula}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    # fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    # portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Many to many puede estar en cualquiera de las 2, pero no en las 2
    # estudiantes = models.ManyToManyField(Estudiante) Lo saco de aquí si se define en trabajar
    # con otro modelo si quiero agregar otro campo como nota
    estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion')

    def __str__(self) -> str:
        return self.nombre


class Inscripcion(models.Model):

    ESTADOS = [
        (1, 'Inscripto'),
        (2, 'Cursando'),
        (3, 'Egresado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS, default=1)

    def __str__(self):
        return f'{self.id} - {self.estudiante} - {self.curso}'

    class Meta:
        verbose_name_plural = "Inscripciones"
