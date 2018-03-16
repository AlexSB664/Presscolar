from django.shortcuts import render
from django.views import generic
from . import models 
from django.urls import reverse_lazy

# Create your views here.
class RegisterMaestro(generic.CreateView):
	template_name="maestros/create.html"
	model = models.maestros
	fields = "__all__"
	success_url = reverse_lazy("alumnos_reporte")
	