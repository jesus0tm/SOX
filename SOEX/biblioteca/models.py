from django.db import models

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    num_paginas = models.IntegerField()