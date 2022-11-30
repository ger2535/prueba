from django.db import models


class Prueba(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.FloatField()
    cantidad = models.IntegerField()