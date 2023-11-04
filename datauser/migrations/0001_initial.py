# Generated by Django 4.2 on 2023-09-27 02:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_stack', models.CharField(max_length=100, verbose_name='Nombre de Stack')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Stack',
                'verbose_name_plural': 'Tecnicas Usadas',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100, verbose_name='Competencias')),
                ('level', models.CharField(choices=[('Basico', 'Basico'), ('Intermedio', 'Intermedio'), ('Alto', 'Alto'), ('Avanzado', 'Avanzado')], max_length=100, verbose_name='Nivel')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='ProjectDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100, verbose_name='Nombre de Proyecto')),
                ('resume_project', models.TextField(verbose_name='Descripcion')),
                ('url_repo', models.URLField(verbose_name='Url Repositorio')),
                ('year_production', models.PositiveIntegerField(blank=True, null=True, verbose_name='Año en Producción')),
                ('developing', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('stack', models.ManyToManyField(to='datauser.stack', verbose_name='Tecnologias Usadas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Proyectos Desarrollados',
            },
        ),
        migrations.CreateModel(
            name='HobbiesExtras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=200, verbose_name='Afición/Pasatiempo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hobbies - Extras',
            },
        ),
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.CharField(choices=[('Clientes', 'Clientes'), ('Proyectos', 'Proyectos'), ('Horas de Soporte', 'Horas de Soporte'), ('Hard Workers', 'Hard Workers')], max_length=25, verbose_name='Hechos')),
                ('value', models.PositiveIntegerField(verbose_name='Total')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hechos',
            },
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=256, verbose_name='Empresa')),
                ('position', models.CharField(max_length=150, verbose_name='Cargo')),
                ('job_description', ckeditor.fields.RichTextField(verbose_name='Funciones Desempeñadas')),
                ('start_date', models.DateField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Culminación')),
                ('still_work', models.BooleanField(default=False, verbose_name='Aún trabajo allí')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('stack', models.ManyToManyField(to='datauser.stack', verbose_name='Tecnologias Usadas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Historia Laboral',
            },
        ),
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_degree', models.CharField(choices=[('Primaria', 'Primaria'), ('Bachillerato', 'Bachillerato'), ('Curso', 'Curso'), ('Tecnico', 'Tecnico'), ('Tecnologo', 'Tecnologo'), ('Pregrado', 'Pregrado'), ('Posgrado', 'Posgrado')], max_length=150, verbose_name='Tipo de Educación')),
                ('academy_name', models.CharField(max_length=150, verbose_name='Institución Educativa')),
                ('degree_obtained', models.CharField(max_length=50, verbose_name='Grado Obtenido')),
                ('degree_esp', models.CharField(blank=True, max_length=50, null=True, verbose_name='Especialidad del Grado')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio de Estudios')),
                ('finish_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Graduación')),
                ('in_progress', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Formacion Académica',
            },
        ),
    ]
