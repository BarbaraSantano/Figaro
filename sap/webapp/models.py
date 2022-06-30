from django.db import models


# Create your models here.

class Lecciones(models.Model):
    nombre_lecciones = models.CharField(max_length=255)
    horas = models.IntegerField()
    temario = models.FileField(null=True, upload_to='static/')

    def __str__(self):
        return f'Lecciones{self.id}: {self.nombre_lecciones} {self.horas} {self.temario}'


class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=255)
    email_profesor = models.EmailField(blank=True, null=True)
    telefono_profesor = models.CharField(max_length=12, null=True)
    lecciones = models.ForeignKey(Lecciones, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Profesor {self.id}: {self.nombre_profesor} {self.email_profesor} {self.telefono_profesor}'


class Alumnos(models.Model):
    nombre_alumnos = models.CharField(max_length=255)
    telefono_alumnos = models.CharField(max_length=12, null=True)
    email_alumnos = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'Alumnos {self.id}: {self.nombre_alumnos} {self.email_alumnos} {self.telefono_alumnos}'


class Calificaciones(models.Model):
    nota = models.IntegerField()
    lecciones = models.ForeignKey(Lecciones, on_delete=models.SET_NULL, null=True)
    alumnos = models.ForeignKey(Alumnos, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Calificaciones {self.id}: {self.nota}'
