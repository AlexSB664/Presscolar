from django.db import models
from padres.models import Tutor
from django.urls import reverse
#from maestros.models import maestros
# Create your models here.

class alumnos(models.Model):
    alu_nombre = models.CharField(max_length = 400)
    alu_genero = models.CharField(max_length = 10,default="none")
    alu_tutores = models.ManyToManyField(Tutor)
    alu_vigente = models.BooleanField(default = True)
    alu_fechaIngreso = models.DateField(auto_now_add = True, null=True)
    alu_observaciones = models.CharField(max_length = 2000, null=True)
    alu_foto = models.ImageField(upload_to='media/fotosAlu', null=True, default='media/default/default.jpeg')
    slug = models.SlugField(max_length=24, default="1")
    
    def __str__(self):
        return self.alu_nombre