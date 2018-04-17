from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tutor(models.Model):
    tut_nombre = models.CharField(max_length=70)
    tut_apellidoPaterno = models.CharField(max_length=70)
    tut_apellidoMaterno = models.CharField(max_length=70)
    tut_numero = models.CharField(max_length = 15, null = True)
    tut_parentesco = models.CharField(max_length = 15, null = True)
    tut_usuario = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    tut_correo = models.CharField(max_length = 15, null = True)
    tut_descripcion = models.CharField(max_length = 15, null = True)
    tut_domicilio = models.CharField(max_length = 400, null = True)
    tut_usurio = models.CharField(max_length = 18, default = 'papasito')
    
    def __str__(self):
        return self.tut_nombre