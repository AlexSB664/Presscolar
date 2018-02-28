from django.db import models
from alumnos.models import alumnos
from django.contrib.auth.models import User

# Create your models here.

class maestros(models.Model):
    mae_nombre = models.OneToOneField(User, on_delete= models.CASCADE)
    mae_apellidoPaterno =models.CharField(max_length=70)
    mae_apellidoMaterno = models.CharField(max_length=70)
    mae_fechaNacimento = models.DateField()
    
    def __str__(self):
        return self.mae_nombre

class grupos(models.Model):
    gru_clave = models.CharField(max_length = 10)
    gru_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, blank=True, null=True, related_name="Maestro")
    gru_alumnos = models.ManyToManyField(alumnos)
    gru_salon = models.CharField(max_length = 10, default='')
    
    def __str__(self):
        return self.gru_clave
    
    
    
    
    
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