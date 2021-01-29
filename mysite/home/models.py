from django.db import models
from django.contrib.auth.models import User
# Create your models here.

g = [None, "1ero", "2ndo", "3ero", "4to", "5to", "6to"]

class Nivel(models.Model):
    nivel = models.CharField(max_length=64, choices=[
        ("Primaria", "Primaria"),
        ("Secundaria", "Secundaria")
    ])
    def __str__(self):
        return self.nivel
    class Meta:
        verbose_name_plural="Niveles"

class Grado(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    grado = models.IntegerField(choices=[
        (i, g[i])
        for i in range(1,7)
    ])
    def __str__(self):
        return f"{g[self.grado]} de {self.nivel}"

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=128)
    grado = models.OneToOneField(Grado, on_delete=models.CASCADE)
    estatus_de_inscripcion = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} de {self.escuela}"