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

# Create your views here.
#class RegisterMaestro(generic.CreateView):
#	template_name="maestros/create.html"
#	model = models.maestros
#	fields = "__all__"
#	success_url = reverse_lazy("alumnos_reporte")

#class StudentSignUpView(CreateView):
#    model = models.User
#    form_class = StudentSignUpForm
#    template_name = 'maestros/create.html'
#
#    def get_context_data(self, **kwargs):
#        kwargs['user_type'] = 'student'
#        return super().get_context_data(**kwargs)
#
#    def form_valid(self, form):
#        user = form.save()
#        login(self.request, user)
#        return redirect('students:quiz_list')

    
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
        m.pro_apellidoPaterno = form.cleaned_data["paterno"]
        m.pro_apellidoMaterno = form.cleaned_data["materno"]
        m.pro_fechaNacimento = form.cleaned_data["nacimiento"]
        m.save()
        return super(agregarMaestro, self).form_valid(form)