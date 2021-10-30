from django.shortcuts import render, HttpResponse
from mainApp.models import Estudiante

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def prueba(request):

    nombre = 'pepe'
    apellido = 'perez'
    estado = True

    estudiantes = mostrar_alumnos()

    return render(request, 'prueba.html',{
        'nomb' : nombre,
        'apell' : apellido,
        'dato' : estudiantes,
        'estado' : estado
    })

def guardar_alumno(request, nombre, documento, telefono):

    estudiante = Estudiante(
        nombre = nombre,
        documento = documento,
        telefono = telefono
    )

    estudiante.save()

    return HttpResponse(f'Estudiante alamcenado: {estudiante.nombre} - cc. {estudiante.documento}')

def mostrar_alumno(request):

    estudiante = Estudiante.objects.get(id = 3)

    return HttpResponse(f'Estudiante encontrado: {estudiante.nombre}') 

def mostrar_alumnos():

    estudiante = Estudiante.objects.all()

    return estudiante