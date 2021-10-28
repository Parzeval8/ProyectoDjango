# Generated by Django 3.2.8 on 2021-10-23 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('observaciones', models.CharField(max_length=255)),
                ('creditos', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('documento', models.IntegerField()),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante_x_Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=15)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.curso')),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.estudiante')),
            ],
        ),
    ]