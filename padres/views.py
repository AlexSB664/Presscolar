from django.shortcuts import render
from .models import Tutor
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Permission
from django.contrib import auth
from django.http import HttpResponseRedirect
from .forms import AddTutorForm
from django.views import generic
from alumnos.models import alumnos
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
            ctx = '';
            if user.is_staff == False:    
                if user.has_perm('padres.is_teacher'):
                    #tut = Tutor.objects.get(username = user.username)
                    #alm = alumnos.objects,get(alu_tutores = tut)
                    print('aaaa')
                    ctx = {'data': 'a'}
                    
                if user.has_perm('padres.is_tutorr'):
                    print('aaaaSSSSS')
                    ctx = {'data':'s'}
                
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            return  HttpResponseRedirect('login/')
    else:
        return render(request, 'log/in.html')

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
        Usr.first_name = form.cleaned_data['fname']
        Usr.last_name = form.cleaned_data['lname']
        prm = Permission.objects.get(codename='is_tutorr')
        Usr.user_permissions.add(prm)
        #Usr.save()
        tut = Tutor()
        tut.tut_nombre = Usr
        tut.tut_descripcion = form.cleaned_data['descrip']
        tut.tut_domicilio = form.cleaned_data['domicilio']
        tut.tut_numero = form.cleaned_data['telefono']
        tut.tut_parentesco = form.cleaned_data['parent']
        tut.save()
        return super(addTutor,self).form_valid(form)
        #return HttpResponseRedirect('maestros/agregar/')
    #else:
     #   return HttpResponseRedirect('maestros/agregar/')
        