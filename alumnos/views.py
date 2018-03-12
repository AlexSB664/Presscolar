from django.shortcuts import render
from alumnos.models import alumnos
from django.views.generic import CreateView, ListView
from alumnos.forms import Alumno_Form
from django.urls import reverse_lazy

def Index(request):
	return render(request,'alumnos/index.html')


#def Alumno_Formulario(request):
#	form = Alumno_Form(request.POST or None)
#	if request.method == "POST":
#		if form.is_valid():
#			form.save()
#	return render(request,'alumnos/formulario.html',{"form":form})
class AlumnoCreate(CreateView):
	model = alumnos
	fields = "__all__"
	template_name = "alumnos/crear.html"
	success_url = reverse_lazy("alumnos_reporte")

class AlumnoReporte(ListView):
	template_name = "alumnos/reporte.html"
	model = alumnos