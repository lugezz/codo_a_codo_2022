# Generated by Django 4.1.1 on 2022-11-03 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cac.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('dni', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cac.persona')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creacion')),
                ('estado', models.IntegerField(choices=[(1, 'Inscripto'), (2, 'Cursando'), (3, 'Egresado')], default=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cac.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cac.estudiante')),
            ],
            options={
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(through='cac.Inscripcion', to='cac.estudiante'),
        ),
    ]
