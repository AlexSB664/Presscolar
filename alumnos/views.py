from django.shortcuts import render
from alumnos.models import alumnos
from django.views.generic import CreateView, ListView,DetailView, UpdateView, DetailView, FormView
from alumnos.forms import Alumno_Form, Alumno_Chido, Alumno_Eva
from django.urls import reverse_lazy
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from padres.models import Tutor, Profesor
from maestros.models import Evaluacion
import string

def Index(request):
    user = request.user
    if user.is_active is True:
        if user.is_staff is False :
            if user.has_perm('padres.is_teacher'):
                prf = Profesor.objects.filter(pro_nombre = user)
                ctx = {'Grupo': 'a', 'Perfil': prf, 'Alumnos': 'akumos'}
                
            if user.has_perm('padres.is_tutorr'):
                tur = Tutor.objects.get(tut_nombre = user)
                alm = alumnos.objects.filter(alu_tutores__in = [tur])
                ctx = {'Alumno':alm}        
            
            return render(request,'alumnos/index.html', ctx)
        else:
            return render(request,'alumnos/index.html')
        
    return render(request,'alumnos/index.html')

#import random, string
#x = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16 ))

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
        datos = []
        filtro = request.GET['filtro']
        data =  Tutor.objects.select_related().filter(tut_apellidos__contains = filtro)
        for dt in data:
            datos.append({"Usuario": str(dt.tut_nombre.username), 'Apellidos': str(dt.tut_apellidos), 'Numero':str(dt.tut_numero), 'Descripcion':str(dt.tut_descripcion)})

        data = serializers.serialize('json',data)
    else:
        data = ""
    return HttpResponse(str(datos))

class ReporteNoChafa(ListView):
	template_name="alumnos/reporte_no_chafa.html"
	model = alumnos #alumnos.object.all()
	paginate_by = 5

    #def get_context_data(self,**kwargs):
    #    obj = self.get_object()
    #    dic={
    #        "name:"obj.name.username,
    #        "aldea:"obj.aldea,
    #        "nature chakra:"obj.nature_chakra
    #    }
    #    return dic
    #
    #def render_to_response(self):
    #    return self
    #
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
    
class Update_Alumno(UpdateView):
    template_name = 'alumnos/updateA.html'
    model = alumnos
    fields = '__all__'
    success_url = reverse_lazy('alumnos_reporte')
    
class Detail_Alumno(DetailView):
    template_name="alumnos/detalleAlumno.html"
    model = alumnos

class AgregarAlumConEstilo(FormView):
    template_name = "alumnos/crear.html"
    form_class = Alumno_Chido
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        alu = alumnos()
        alu.alu_nombre = form.cleaned_data['alu_nombre']
        alu.alu_genero = form.cleaned_data['alu_genero']
        #alu.alu_tutores = form.cleaned_data['alu_tutores']
        alu.save()
        alu.alu_tutores.set(form.cleaned_data['alu_tutores'])
        alu.alu_vigente = form.cleaned_data['alu_vigente']
        alu.alu_fechaIngreso = form.cleaned_data['alu_fechaIngreso']
        alu_observaciones = form.cleaned_data['alu_observaciones']
        alu.save()
        return super(AgregarAlumConEstilo,self).form_valid(form)

class EvaluarAlumno(FormView):
    template_name = "alumnos/evaluar.html"
    form_class = Alumno_Eva
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        alu = Evaluacion()
        alu.alu_nombre = form.cleaned_data['alu_nombre']
        alu.alu_genero = form.cleaned_data['alu_genero']
        #alu.alu_tutores = form.cleaned_data['alu_tutores']
        alu.save()
        alu.alu_tutores.set(form.cleaned_data['alu_tutores'])
        alu.alu_vigente = form.cleaned_data['alu_vigente']
        alu.alu_fechaIngreso = form.cleaned_data['alu_fechaIngreso']
        alu_observaciones = form.cleaned_data['alu_observaciones']
        alu.save()
        return super(AgregarAlumConEstilo,self).form_valid(form)
