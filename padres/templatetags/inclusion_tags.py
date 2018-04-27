from django import template
from alumnos.models import alumnos
from padres.models import Tutor
from django.contrib.auth.models import User
from padres import views

register = template.Library()

@register.inclusion_tag('alumnos/infoTutor.html')
def infoAlumno():
    usr = User.objects.get(username = 'corita')
    #usr = request.user
    tu = Tutor.objects.get(tut_nombre = usr)
    al = alumnos.objects.get(alu_tutores = tu )
    return {'alumno': al}