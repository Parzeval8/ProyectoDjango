from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha_nac = models.DateField(null=True, blank=True)
    telefono = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Curso(models.Model):
    nombre = models.CharField(max_length=10)
    observaciones = models.CharField(max_length=255)
    creditos = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Estudiante_x_Curso(models.Model):
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

