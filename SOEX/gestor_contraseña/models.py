from django.db import models

# Create your models here.

class contraseñas(models.Model):
    nombre = models.CharField()
    contraseña = models.CharField(max_length=100)
