from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

GRADOS = [
    "1° de Primaria",
    "2° de Primaria",
    "3° de Primaria",
    "4° de Primaria",
    "5° de Primaria",
    "6° de Primaria",
    "1° de Secundaria",
    "2° de Secundaria",
    "3° de Secundaria"
]

GRUPOS = [
    "ESTUDIANTES 1",
    "ESTUDIANTES 2",
    "ESTUDIANTES 3",
    "ESTUDIANTES 4"
]

GRUPO_POR_GRADO = [
    "ESTUDIANTES 1",
    "ESTUDIANTES 1",
    "ESTUDIANTES 1",
    "ESTUDIANTES 2",
    "ESTUDIANTES 2",
    "ESTUDIANTES 3",
    "ESTUDIANTES 3",
    "ESTUDIANTES 4",
    "ESTUDIANTES 4"
]

class Estudiante(models.Model):
    """
    Modelo que representa al estudiante en la base de datos
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=128)
    grado = models.IntegerField(choices=[
        (i, GRADOS[i])
        for i in range(9)
    ])
    estatus_de_inscripcion = models.IntegerField(default=0)
    matricula = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} de {self.escuela}"

class Actividad(models.Model):
    nombre = models.CharField(max_length=128)
    tiempo = models.DateTimeField()
    dura = models.DurationField()
    link = models.URLField(default="www.google.com")
    invitados = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name_plural = "Actividades"
        ordering = ['tiempo', 'nombre']

    def __str__(self):
        return self.nombre