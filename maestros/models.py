from django.db import models
from alumnos.models import alumnos
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db.models.manager import EmptyManager

# Create your models here.
class User(AbstractUser):
    es_padre = models.BooleanField('estado de padre', default=False)
    es_maes = models.BooleanField('estado de maestro', default=False)
    groups = EmptyManager(Group)
    user_permissions = EmptyManager(Permission)



class maestros(models.Model):
    mae_nombre = models.OneToOneField(User, on_delete= models.CASCADE)
    mae_apellidoPaterno =models.CharField(max_length=70)
    mae_apellidoMaterno = models.CharField(max_length=70)
    mae_fechaNacimento = models.DateField()
    
    def __str__(self):
        return str(self.mae_nombre)

class grupos(models.Model):
    gru_clave = models.CharField(max_length = 10)
    gru_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, blank=True, null=True, related_name="Maestro")
    gru_alumnos = models.ManyToManyField(alumnos)
    gru_salon = models.CharField(max_length = 10, default='')
    gru_grado = models.IntegerField(null=True)
    
    def __str__(self):
        return self.gru_clave

class grupoAlumno(object):
    grupoFo = models.ForeignKey(grupos,on_delete=models.CASCADE,related_name="Grupo")
    """docstring for grupoAlumno"""
    def __init__(self, arg):
        super(grupoAlumno, self).__init__()
        self.arg = arg
        
    
class DiarioTrabajo(models.Model):
    DT_maestro = models.ForeignKey(maestros, on_delete = models.CASCADE)
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