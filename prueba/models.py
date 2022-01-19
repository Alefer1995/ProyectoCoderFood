from django.db import models

class Curso(models.Model):
    curso=models.CharField(max_length=100)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Recetas(models.Model):
    nombreReceta= models.CharField(max_length=30)
    ingredientes= models.CharField(max_length=100)
    instrucciones= models.CharField(max_length=500) 
    enviar = models.BooleanField()