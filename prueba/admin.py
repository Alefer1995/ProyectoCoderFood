from django.contrib import admin

from prueba.models import Curso, Estudiante, Profesor, Recetas

# Register your models here.

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Recetas)

