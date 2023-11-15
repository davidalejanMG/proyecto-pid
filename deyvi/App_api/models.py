from django.db import models
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=50)
    año = models.IntegerField()

# Create your models here.
