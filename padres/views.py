from django.shortcuts import render
from .models import Tutor
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Permission
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .forms import AddTutorForm
from django.views import generic
from alumnos.models import alumnos
import json
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def LogIn(request):    
	return render(request,'log/in.html')

def Index2(request):    
	return render(request,'padres/indexPadres.html')
    
def login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            return  HttpResponseRedirect('login/')
    else:
        return render(request, 'log/in.html')

def updateTutores(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        alm = alumnos.objects.get(slug = slug)
        tuto = json.loads(request.POST['alu_tutores'])
        alm.alu_tutores.clear()
        alm.save()
        for x in range(len(tuto)):
            tut = (tuto[x]['Usuario'])
            usu = User.objects.get(username = tut)
            tutor = Tutor.objects.get(tut_nombre = usu)
            alm.alu_tutores.add(tutor)
        alm.save()
    
    return HttpResponseRedirect('/')

class addTutor(generic.FormView):
    template_name = 'padres/agregar.html'
    form_class = AddTutorForm
    success_url = reverse_lazy('AddTutor')
    
    def form_valid(self, form):
        Usr = form.save()
        #Usr = User()
        #username = request.POST['username']
        #password = request.POST['password']
        #Usr.username = username
        #Usr.password = password
        prm = Permission.objects.get(codename='is_tutorr')
        Usr.user_permissions.add(prm)
        #Usr.save()
        tut = Tutor()
        tut.tut_nombre = Usr
        tut.tut_apellidos = form.cleaned_data['fname'] + ' ' + form.cleaned_data['lname'] + ' ' + form.cleaned_data['apellidoM']
        tut.tut_descripcion = form.cleaned_data['descrip']
        tut.tut_domicilio = form.cleaned_data['domicilio']
        tut.tut_numero = form.cleaned_data['telefono']
        tut.tut_parentesco = form.cleaned_data['parent']
        tut.save()
        return super(addTutor,self).form_valid(form)
        #return HttpResponseRedirect('maestros/agregar/')
    #else:
     #   return HttpResponseRedirect('maestros/agregar/')
        
def tutorAsign(request, slug):
    dat = slug
    almn = alumnos.objects.get(slug = dat)
    tutores = []
    for aln in almn.alu_tutores.all():
        ud = User.objects.get(username = aln)
        pad = Tutor.objects.get(tut_nombre = ud)
        tutores.append({'Apellidos':pad.tut_apellidos})
    
    print(tutores)
    ctx = {'Alumno': almn, 'Padres': tutores}
    return render(request, 'alumnos/alumnotutores.html', ctx)
