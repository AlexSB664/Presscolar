from django.db import models
from padres.models import Tutor
from django.urls import reverse
#from maestros.models import maestros
# Create your models here.

class alumnos(models.Model):
    alu_nombre = models.CharField(max_length = 400)
    alu_tutores = models.ManyToManyField(Tutor)
    alu_vigente = models.BooleanField(default = False)
    alu_fechaIngreso = models.DateField(auto_now_add = True, null=True)
    alu_observaciones = models.CharField(max_length = 2000, null=True)
    alu_foto = models.ImageField(upload_to='media/fotosAlu', null=True)
    
    def __str__(self):
        return self.alu_nombre