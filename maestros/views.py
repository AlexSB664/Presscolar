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
from django.core import serializers
import json

class agregarMaestro(FormView):
    template_name = 'maestros/addTeacher.html'
    form_class = StudentSignUpForm
    success_url =reverse_lazy('reporteMaestro')
    
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

def actualizaGrupo(request,slug):
    ng = grupos.objects.select_related().get(id=slug)
    maestro = Profesor.objects.exclude(pro_nombre = ng.gru_maestro.pro_nombre).all()
    if request.method == 'POST':
        us = User.objects.get(username= request.POST['maestro'])  
        mae = Profesor.objects.get(pro_nombre = us)
        ng.gru_clave = request.POST['clave']
        ng.gru_salon = request.POST['salon']
        ng.gru_maestro = mae
        ng.gru_grado = int(request.POST['grado'])
        ng.gru_alumnos.clear()
        ng.save()
        alms = json.loads(request.POST['alumnos'])
        for j in range(len(alms)):
            almSave = alumnos.objects.get(slug = alms[j]['slug'])    
            ng.gru_alumnos.add(almSave)
        ng.save()
    

    ng = grupos.objects.select_related().get(id = slug)
    maestro = Profesor.objects.exclude(pro_nombre = ng.gru_maestro.pro_nombre).all()
    alumnosGrupo = grupos.objects.select_related().get(id=slug)
    datosAlumnos = []
    for x in alumnosGrupo.gru_alumnos.all():
        datosAlumnos.append({"slug":x.slug, "Nombre": x.alu_nombre})

    ctx = {"Grupo":ng, "Maestro": ng.gru_maestro, "Profesores": maestro, "Alumnos": datosAlumnos}
    return render(request, 'grupos/actualizagrupo.html', ctx)        

def buscarEnelGrupo(request,slug):
    if request.method == 'GET':
        filtro = request.GET['filtro']
        almg = grupos.objects.select_related().exclude(id=slug).all()
        alm = []
        for ix in almg:
            for x in ix.gru_alumnos.all():
                alm.append(x.id)

        alumnosF = alumnos.objects.exclude(id__in = alm).filter(alu_nombre__contains = filtro)
        data = serializers.serialize('json', alumnosF)

    return HttpResponse(data)



def crearGrupo(request):
    if request.method == 'POST':
        ng = grupos()
        ng.gru_clave = request.POST['clave']
        ng.gru_salon = request.POST['salon']
        ng.gru_grado = int(request.POST['grado'])
        ng.save()
        alms = json.loads(request.POST['alumnos'])
        for i in range(len(alms)):
            addl = alumnos.objects.get(slug = alms[i]['slug'])
            ng.gru_alumnos.add(addl)

        ng.save()
        us = User.objects.get(username = request.POST['maestro'])
        pro = Profesor.objects.get(pro_nombre = us)
        ng.gru_maestro = pro;
        ng.save()


    gps = grupos.objects.select_related().all()
    maes = Profesor.objects.all()
    data = []
    for gp in gps:
        for alm in gp.gru_alumnos.all():
            data.append(alm.slug)
    

    alm = alumnos.objects.exclude(slug__in = data).all()
    return render(request, 'grupos/agregargrupo.html', {"Alumnos": alm, 'Maestros': maes})

def buscarSinGrupo(request):
    if request.method == 'GET':
        filtro = request.GET['filtro']
        gps = grupos.objects.select_related().all()
        alums = []
        for x in gps:
            for alm in x.gru_alumnos.all():
                alums.append(alm.slug)

        alm = alumnos.objects.exclude(slug__in =alums).filter(alu_nombre__contains = filtro)
        data = serializers.serialize('json',alm)

    return HttpResponse(data)

class GrupoReporte(generic.ListView):
    template_name = 'grupos/reporte.html'
    model = grupos

def buscarGrupo(request):
    if request.method == 'GET':
        filtro = request.GET['filtro']
        grp = grupos.objects.select_related().filter(Q(gru_salon__contains = filtro) |Q(gru_clave__contains = filtro))
        tut = []
        for x in grp:
            tut.append({"Tutor": str(x.gru_maestro.pro_nombres + ' ' + x.gru_maestro.pro_apellidoPaterno), "Clave": x.gru_clave, "Salon": x.gru_salon, "Grado": x.gru_grado, "Id": x.id, "Alumnos": len(x.gru_alumnos.all())})

    return HttpResponse(str(tut))

def infoGrupo(request, slug):
    grp = grupos.objects.select_related().get(id = slug)
    ctx = {"Grupo": grp, "Alumnos": grp.gru_alumnos.all(), "Profesor": grp.gru_maestro}
    return render(request, 'grupos/detallegrupo.html', ctx)
