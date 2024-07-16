from django.db import models

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    compradoPor = models.CharField(max_length=50, default='')
    isActive = models.BooleanField(default=True)
    

