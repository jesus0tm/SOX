from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()