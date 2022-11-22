from django import forms
from django.forms import ValidationError

from cac.models import Categoria, CursoM, EstudianteM, Proyecto


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})


class ContactoForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre',
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            )
    asunto = forms.CharField(
            label='Asunto',
            max_length=100,
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    subscripcion = forms.BooleanField(
            label='Desea suscribirse a los mails de Codo a Codo',
            required=False,
            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
        )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']

        if len(data) < 10:
            raise ValidationError('Debes especificar mejor el mensaje')

        return data

    def clean(self):
        cleaned_data = super().clean()
        mensaje = cleaned_data.get("mensaje")
        asunto = cleaned_data.get("asunto")

        if "ayuda" not in asunto and "ayuda" not in mensaje:
            msg = "Debe agregar la palabara 'ayuda' en el campo."
            self.add_error('asunto', msg)
            self.add_error('mensaje', msg)


class CategoriaForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model = Categoria
        # fields='__all__'
        fields = ['nombre']
        # exclude=('baja',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre'})
        }
        error_messages = {
            'nombre': {
                'required': 'No te olvides de mi!'
            }
        }


class CategoriaFormValidado(CategoriaForm):

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre.upper() == 'ORIGAMI':
            raise ValidationError('Codo a Codo no dicta cursos de esta temática')
        return nombre


class CursoForm(forms.ModelForm):

    class Meta:
        model = CursoM
        fields = ['nombre', 'fecha_inicio', 'portada', 'descripcion', 'categoria']

    nombre = forms.CharField(
            label='Nombre',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    fecha_inicio = forms.DateField(
            label='Fecha Inicio',
            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )


class EstudianteMForm(forms.ModelForm):

    class Meta:
        model = EstudianteM
        fields = ['nombre_m', 'apellido_m', 'email_m', 'dni_m', 'matricula_m']
        widgets = {
            'nombre_m': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class': 'form-control'}),
            'email_m': forms.EmailInput(attrs={'class': 'form-control'}),
            'dni_m': forms.NumberInput(attrs={'class': 'form-control'}),
            'matricula_m': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'anio', 'url', 'portada', 'estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'portada': forms.FileInput(attrs={'class': 'form-control'}),
            'estudianteM': forms.Select(attrs={'class': 'form-control'}),
        }
