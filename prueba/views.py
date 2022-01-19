from django.shortcuts import render
from prueba.models import Curso, Estudiante, Profesor, Recetas

def index(req):
    return render(req, 'index.html')

def prueba(req):

    lista = Curso.objects.all()

    return render(req, 'cursos.html', {"lista": lista})

def herenciaHijo2(req):

    lista = Recetas.objects.all()

    return render(req, 'recetas.html', {"lista": lista})

