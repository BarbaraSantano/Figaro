from django.http import HttpResponse

# Create your views here.
from webapp.forms import AlumnosForm
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import *

def login(request):
    # return HttpResponse('Holaaa')
    return render(request, 'index.html')


def inicio(request):
    # return HttpResponse('Holaaa')
    return render(request, 'home.html')

def registro(request):
    return render(request, 'registro.html')


def contraseña(request):
    return render(request, 'contraseña.html')


def recuperada(request):
    return render(request, 'recuperada.html')

def alumnos(request):
    nombre_alumnos = Alumnos.objects.all()
    #alumno = Alumnos.objects.order_by()
    return render(request, 'alumnos.html', {'alumnos': nombre_alumnos})

def lecciones(request):
    nombre_lecciones = Lecciones.objects.all()
    # alumno = Alumnos.objects.order_by()
    return render(request, 'lecciones.html', {'lecciones': nombre_lecciones})

def calificaciones(request):
    nota = Calificaciones.objects.all()
    return render(request, 'calificaciones.html', {'calificaciones': nota})

def alumnoNuevo(request):
    if request.method == 'POST':
        formaAlumnos = AlumnosForm(request.POST)
        if formaAlumnos.is_valid():
            formaAlumnos.save()
            return redirect('alumno')

    else:
        formaAlumnos = AlumnosForm

        return render(request, 'nuevoAlumno.html', {'foralumno': formaAlumnos})

def editarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    if request.method == 'POST':
        formaAlumnos = AlumnosForm(request.POST, instance=alumno)
        if formaAlumnos.is_valid():
            formaAlumnos.save()
            return redirect('alumno')

    else:
        formaAlumnos = AlumnosForm(instance=alumno)

    return render(request, 'editar.html', {'foralumno': formaAlumnos})

def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    if alumno:
        alumno.delete()
    return redirect('alumno')

