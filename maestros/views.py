from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views import generic
from . import models 
from django.urls import reverse_lazy
from django.views.generic import CreateView
#example for diferent sessions
from .forms import StudentSignUpForm

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
	