from django.db import models
from django.contrib.auth.models import User #, AbstractUser, Group, Permission
from django.db.models.manager import EmptyManager
from django.utils.translation import ugettext as _
from datetime import datetime
# Create your models here.

class Tutor(models.Model):
    tut_nombre = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    tut_apellidos = models.CharField(max_length = 60, null = True)
    tut_numero = models.CharField(max_length = 15, null = True)
    tut_parentesco = models.CharField(max_length = 15, null = True)
    tut_descripcion = models.CharField(max_length = 15, null = True)
    tut_domicilio = models.CharField(max_length = 400, null = True)
    
    
    def __str__(self):
        return self.tut_nombre.username
    
    class Meta:
        
        permissions = (
            ('is_tutorr', 'Is_Tutorr'),
        )
    
    
class Profesor(models.Model):
    pro_nombre = models.OneToOneField(User, on_delete= models.CASCADE, null = True)
    pro_apellidoPaterno =models.CharField(max_length=70, default = 's')
    pro_apellidoMaterno = models.CharField(max_length=70, default = 's')
    pro_fechaNacimento = models.DateField(default = datetime.now, blank = True)
    
    def __str__(self):
        return str(self.pro_nombre.username)
    
    class Meta:
        
        permissions = (
            ('is_teacher', 'Is_Teacher'),
        )