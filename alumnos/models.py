from django.db import models
from padres.models import Tutor
# Create your models here.

class alumnos(models.Model):
    alu_nombre = models.CharField(max_length = 400)
    alu_tutores = models.ManyToManyField(Tutor)
    
    def __str__(self):
        return self.alu_nombre
    
#class DiarioTrabajo(models.Models):
#    DT_alumno = models.ForeignKey(alumnos, on_delete= models.CASCADE)
#    DT_