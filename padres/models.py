from django.db import models

# Create your models here.

class Tutor(models.Model):
    tut_nombre = models.CharField(max_length=70)
    tut_apellidoPaterno = models.CharField(max_length=70)
    tut_apellidoMaterno = models.CharField(max_length=70)
    tut_numero = models.CharField(max_length = 15, null = True)
    
    def __str__(self):
        return self.tut_nombre