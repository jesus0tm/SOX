from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    num_paginas = models.IntegerField()