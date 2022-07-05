from django.contrib import admin
from django.urls import path

from webapp.views import *

from webapp.views import *

urlpatterns = [
    path('', login),
    path('perfil/', perfil),
    path('inicio/', inicio),
    path('registro/', registro),
    path('contraseña/', contraseña),
    path('recuperada/', recuperada),
    path('lecciones/', lecciones),
    path('alumnos/', alumnos, name="alumno"),
    path('alumnos/nuevoalumno/', alumnoNuevo, name="nuevoAlumno"),
    path('alumnos/editar/<int:id>', editarAlumno),
    path('alumnos/eliminaralumno/<int:id>', eliminarAlumno),
]
