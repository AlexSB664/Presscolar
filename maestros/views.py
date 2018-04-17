from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views import generic
from . import models 
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
#example for diferent sessions
from .forms import StudentSignUpForm, AltaMaestros
from django.contrib.auth.models import User

# Create your views here.
#class RegisterMaestro(generic.CreateView):
#	template_name="maestros/create.html"
#	model = models.maestros
#	fields = "__all__"
#	success_url = reverse_lazy("alumnos_reporte")

class StudentSignUpView(CreateView):
    model = models.User
    form_class = StudentSignUpForm
    template_name = 'maestros/create.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:quiz_list')

    
class agregarMaestro(FormView):
    template_name = 'maestros/addTeacher.html'
    form_class = AltaMaestros
    succes_url =reverse_lazy('add_teacher')
    
    def form_valid(self, form):
        m = models.maestros()
        name = form.cleaned_data["username"]
        usr = User.objects.get(username = name)
        m.mae_nombre = usr
        m.mae_apellidoPaterno = form.cleaned_data["paterno"]
        m.mae_apellidoMaterno = form.cleaned_data["materno"]
        m.mae_fechaNacimento = form.cleaned_data["nacimiento"]
        m.save()
        return super(agregarMaestro, self).form_valid(form)