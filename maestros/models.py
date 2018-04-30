from django.db import models
from alumnos.models import alumnos
from padres.models import Profesor
from django.db.models.manager import EmptyManager


class grupos(models.Model):
    gru_clave = models.CharField(max_length = 10)
    gru_maestro = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=True, null=True, related_name="Maestro")
    gru_alumnos = models.ManyToManyField(alumnos)
    gru_salon = models.CharField(max_length = 10, default='')
    gru_grado = models.IntegerField(null=True)
    
    def __str__(self):
        return self.gru_clave
        
    
class DiarioTrabajo(models.Model):
    DT_maestro = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    DT_alumno = models.ForeignKey(alumnos, on_delete= models.CASCADE)
    DT_fecha = models.DateField(auto_now_add = True)
    DT_descripcion = models.CharField(max_length = 2000)
    DT_actividadApoyo = models.CharField(max_length = 2000)
    DT_necesidades = models.CharField(max_length = 2000)
    
    def __str__(self):
        return str(self.DT_alumno)
    
    
    
# Create your models here.


#class nombreModelo(models.Model):
#   nombrevalor1 = models.CharField(max_length=18)
#   nombreValor2 = models.CharField(max_length=20) 
#   nombreValor3 = models.FloatField(max_length=20)
#   nombreValor4 = models.IntegerField()
#   nombreValor5 = models.BooleanField(default=false)
#   nombreValor6 = models.DateField(auto_now_add = true)
#   nombreValor7 = models.CharField(max_length=20)
#   nombreValor8 = models.CharField(max_length=20)
#   nombreValor9 = models.CharField(max_length=20)
#   nombreValor0 = models.CharField(max_length=20)

    #def __str__ (self):
        #return self.nombreValorRegresar
        
#class nombreModelo(models.Model):
#   nombrevalor1 = models.CharField(max_length=18)
#   nombreValor2 = models.CharField(max_length=20) 
#   nombreValor3 = models.FloatField(max_length=20)
#   nombreValor4 = models.IntegerField()
#   nombreValor5 = models.BooleanField(default=false)
#   nombreValor6 = models.DateField(auto_now_add = true)
#   nombreValor7 = models.CharField(max_length=20)
#   nombreValor8 = models.CharField(max_length=20)
#   nombreValor9 = models.CharField(max_length=20)
#   nombreValor0 = models.CharField(max_length=20)

    #def __str__ (self):
        #return self.nombreValorRegresar
        
#class nombreModelo(models.Model):
#   nombrevalor1 = models.CharField(max_length=18)
#   nombreValor2 = models.CharField(max_length=20) 
#   nombreValor3 = models.FloatField(max_length=20)
#   nombreValor4 = models.IntegerField()
#   nombreValor5 = models.BooleanField(default=false)
#   nombreValor6 = models.DateField(auto_now_add = true)
#   nombreValor7 = models.CharField(max_length=20)
#   nombreValor8 = models.CharField(max_length=20)
#   nombreValor9 = models.CharField(max_length=20)
#   nombreValor0 = models.CharField(max_length=20)

    #def __str__ (self):
        #return self.nombreValorRegresar