from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views import generic
from . import models 
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
#example for diferent sessions
from .forms import StudentSignUpForm
from padres.models import Profesor
from django.contrib.auth.models import User, Permission
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from .models import grupos
from alumnos.models import alumnos

class agregarMaestro(FormView):
    template_name = 'maestros/addTeacher.html'
    form_class = StudentSignUpForm
    success_url =reverse_lazy('add_teacher')
    
    def form_valid(self, form):
        usr = form.save()
        prm = Permission.objects.get(codename='is_teacher')
        usr.user_permissions.add(prm)
        
        m = Profesor()
        m.pro_nombre = usr
        m.pro_nombres = form.cleaned_data['nombres']
        m.pro_apellidoPaterno = form.cleaned_data["paterno"]
        m.pro_apellidoMaterno = form.cleaned_data["materno"]
        m.pro_fechaNacimento = form.cleaned_data["nacimiento"]
        m.save()
        return super(agregarMaestro, self).form_valid(form)
        
def actualizarMaestro(request,slug):
    usr = User.objects.get(username = slug)
    maes = Profesor.objects.get(pro_nombre = usr)

    if request.method == 'POST':
        usr.set_password(request.POST['password1'])
        usr.save()

        maes.pro_nombres = request.POST['nombres']
        maes.pro_apellidoPaterno = request.POST['paterno']
        maes.pro_apellidoMaterno = request.POST['materno']
        maes.pro_fechaNacimento = request.POST['nacimiento']
        maes.save()

    ctx = {'Maestro':maes, 'Usuario': usr}
    return render(request, 'maestros/actualizamaestro.html', ctx)

class MaestroReporte(generic.ListView):
    template_name = 'maestros/reporte.html'
    model = Profesor

def buscarMaestros(request):
    if request.method == 'GET':
        datos = []
        filtro = request.GET['filtro']
        pfr = Profesor.objects.select_related().filter( Q(pro_nombres__contains = filtro) |Q(pro_apellidoMaterno__contains = filtro) |Q(pro_apellidoPaterno__contains = filtro))
        for x in pfr:
            datos.append({"Usuario":x.pro_nombre.username, "Nombre": (str(x.pro_nombres) + ' ' + str(x.pro_apellidoPaterno) + ' ' + str(x.pro_apellidoMaterno)), "Fecha": str(x.pro_fechaNacimento.strftime('%Y/%m/%d'))})

    else:
        datos = []

    return HttpResponse(str(datos))    

def DetalleMaestro(request, slug):
    usr = User.objects.get(username = slug)
    prf = Profesor.objects.get(pro_nombre = usr)
    grp = grupos.objects.select_related().filter(gru_maestro = prf)

    ctx = {"Usuario":usr, "Profesor": prf, "Grupos": grp}
    return render(request, 'maestros/detallemaestro.html', ctx)

def crearGrupo(request):
    gps = grupos.objects.select_related().all()
    data = []
    for gp in gps:
        for alm in gp.gru_alumnos.all():
            data.append(alm.slug)
            

    alm = alumnos.objects.exclude(slug__in = data).all()
    return render(request, 'grupos/agregargrupo.html', {"Alumnos": alm})
