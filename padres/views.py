from django.shortcuts import render
from .models import Tutor
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
def LogIn(request):    
	return render(request,'log/in.html')

def Index2(request):    
	return render(request,'padres/indexPadres.html')

def iniciopadre(request):
    #print(request.POST['code'])
    mensaje = ''
    buscar = str(request.POST['code'])
    
    usr = User.objects.filter(username = buscar)
    if usr.count() > 0:
        p =  Tutor.objects.filter(tut_usuario=usr)
        if p.count() > 0:
            request.session["padre"] = User
            reverse_lazy('index')
        else:
            mensaje = 'No se encontro usuario existente'
            request.session["padre"] = False
        
    else:
        request.session["padre"] = False
    return render(request,'log/in.html', {'msg': mensaje})