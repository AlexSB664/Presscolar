from django.shortcuts import render
from alumnos.models import alumnos
from django.views.generic import CreateView, ListView,DetailView
from alumnos.forms import Alumno_Form
from django.urls import reverse_lazy
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from padres.models import Tutor

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
    
def busquedaTurores(request):
    if  request.method == 'GET':
        filtro = request.GET['nombre']
        data = serializers.serialize('json', Tutor.objects.filter(tut_nombre__contains = filtro))
        
    else:
        data = ""
    
    print(data)
    return HttpResponse(data, 'application/json')

class ReporteNoChafa(ListView):
	template_name="alumnos/reporte_no_chafa.html"
	model = alumnos #alumnos.object.all()
	paginate_by = 5

def busquedaAlumno(request):
    if request.method == 'GET':
        filtro = request.GET['filtro']
        data = serializers.serialize('json', alumnos.objects.filter(alu_nombre__contains = filtro))
    else:
        data = ""
    return HttpResponse(data)

class Detail_ninja(DetailView):
    template_name="amunlos/detalleAlumno.html"
    model = alumnos