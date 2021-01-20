from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=128)
    primaria_o_secundaria = models.IntegerField()
    grado = models.IntegerField()
    estatus_de_inscripcion = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} de {self.escuela}"