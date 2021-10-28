from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def prueba(request):

    nombre = 'pepe'
    apellido = 'perez'

    return render(request, 'prueba.html',{
        'nomb' : nombre,
        'apell' : apellido,
        'dato' : [12,34,12,567]
    })