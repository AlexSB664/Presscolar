from django.shortcuts import render
from alumnos.models import alumnos
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView,DetailView, UpdateView, DetailView, FormView
from alumnos.forms import Alumno_Form, Alumno_Chido, Alumno_Eva, Alumno_EvaDiario
from django.urls import reverse_lazy
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from padres.models import Tutor, Profesor
from maestros.models import Evaluacion, grupos, DiarioTrabajo
import string
from datetime import date, timedelta, datetime

def get_week_days(year, week):
    d = date(year,1,1)
    if(d.weekday()>3):
        d = d+timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    return d + dlt,  d + dlt + timedelta(days=6)


def Index(request):
    user = request.user
    if user.is_active is True:
        if user.is_staff is False :
            if user.has_perm('padres.is_teacher'):
                yar = datetime.now().year
                today = date.today()
                wk = today.isocalendar()[1]
                inicio, fin = get_week_days(yar ,wk)
                prf = Profesor.objects.get(pro_nombre = user)
                grp = grupos.objects.select_related().filter(gru_maestro = prf)
                almGRUP = []
                for k in grp:
                    almGRUP.append({"Alumnos": k.gru_alumnos.all(), "Grupo": k.id})

                evaluacionesArray = []
                for j in range(len(almGRUP)):
                    kj = []
                    for hj in almGRUP[j]['Alumnos']:
                        kj.append(hj.id)

                    diarios = []
                    amevals = []
                    evalpos = []
                    evals =  Evaluacion.objects.filter(E_alumno__id__in = kj).filter(E_fecha__range = [inicio, fin])
                    for nh in evals:
                        amevals.append(nh.E_alumno.id)
                        evalpos.append({"IDA": nh.E_alumno.id, "EvaId": nh.id})

                    diar = DiarioTrabajo.objects.select_related().filter(DT_fecha = today).filter(DT_alumno__id__in = kj)
                    idDiar = []
                    aluDiar = []           
                    for ml in diar:
                        idDiar.append(ml.id)
                        aluDiar.append(ml.DT_alumno.id)

                    diarios.append({"Diario": idDiar, "Alumno": aluDiar})
                    evaluacionesArray.append({"Grupo": almGRUP[j]['Grupo'], "Alumnos": amevals, "EvalId": evalpos, "Diario": diarios})
                ctx = {"Perfil": prf, "Grupos": grp, "Evaluados": evaluacionesArray}
                print(ctx)
            if user.has_perm('padres.is_tutorr'):
                tur = Tutor.objects.get(tut_nombre = user)
                alm = alumnos.objects.filter(alu_tutores__in = [tur])
                ctx = {"Alumno":alm}        
            
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

class DiarioReporte(ListView):
    template_name="evaluaciones/reporteDiario.html"
    today = date.today()
    model = DiarioTrabajo
    queryset = DiarioTrabajo.objects.filter(DT_fecha__startswith=today)

class EvaluacionReporte(ListView):
    template_name="evaluaciones/reporteEvaluacion.html"
    model = Evaluacion
    date = date.today()
    start_week = date - timedelta(date.weekday())
    end_week = start_week + timedelta(7)
    queryset = Evaluacion.objects.filter(E_fecha__range= [start_week, end_week])

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
    success_url = reverse_lazy('alumnos_reporte')
    
    def form_valid(self, form):
        alu = alumnos()
        alu.alu_nombre = form.cleaned_data['alu_nombre']
        alu.alu_genero = form.cleaned_data['alu_genero']
        #alu.alu_tutores = form.cleaned_data['alu_tutores']
        alu.save()
        gen = form.cleaned_data['alu_genero']
        if gen == 'Masculino':
            alu.alu_foto = 'media/default/boy.png'
        else:
            alu.alu_foto = 'media/default/girl.jpg'
        alu.alu_tutores.set(form.cleaned_data['alu_tutores'])
        alu.alu_vigente = form.cleaned_data['alu_vigente']
        alu.alu_fechaIngreso = form.cleaned_data['alu_fechaIngreso']
        alu.alu_observaciones = form.cleaned_data['alu_observaciones']
        alu.slug =form.cleaned_data['slug']
        alu.save()
        return super(AgregarAlumConEstilo,self).form_valid(form)

class EvaluarAlumno(FormView):
    template_name = "alumnos/evaluar.html"
    form_class = Alumno_Eva
    success_url = reverse_lazy('reporteEvaluacion')

    def get_context_data(self, *args, **kwargs):
        ctx = super(EvaluarAlumno, self).get_context_data(*args, **kwargs)
        #ctx['slug'] = self.kwargs['slug'] # or Tag.objects.get(slug=...)
        slug = self.kwargs['slug']
        ctx ['alumno'] = alumnos.objects.get(slug=slug)
        return ctx
    
    def form_valid(self, form):
        eva = Evaluacion()
        filtro = form.cleaned_data['E_maestro']
        maes = Profesor.objects.get(pro_nombre=filtro)
        eva.E_maestro = maes
        filtroalum = form.cleaned_data['E_alumno']
        alu = alumnos.objects.get(alu_nombre=filtroalum)
        eva.E_alumno = alu
        #eva = Evaluacion()
        #filtro = form.cleaned_data['E_maestro']
        #maeusr = User.objects.get(username = filtro)
        #maes = Profesor.objects.get(pro_nombre=maeusr)
        #eva.E_maestro = maes
        #filtroalum = form.cleaned_data['E_alumno']
        #alu = alumnos.objects.get(alu_nombre=filtroalum)
        #eva.E_alumno = alu
        eva.E_fecha = form.cleaned_data['E_fecha']
        eva.E_comparte = form.cleaned_data['E_comparte']
        eva.E_apoya =  form.cleaned_data['E_apoya']
        eva.E_pregunta =  form.cleaned_data['E_pregunta']
        eva.E_sugerencia =  form.cleaned_data['E_sugerencia']
        eva.E_controla = form.cleaned_data['E_controla']
        eva.E_cuida =  form.cleaned_data['E_cuida']
        eva.E_espera =  form.cleaned_data['E_espera']
        eva.E_negocia =  form.cleaned_data['E_negocia']
        eva.E_trabajaEquipo =  form.cleaned_data['E_trabajaEquipo']
        eva.E_respeta =  form.cleaned_data['E_respeta']
        eva.E_cuidadoso =  form.cleaned_data['E_cuidadoso']
        eva.E_involucra =  form.cleaned_data['E_involucra']
        eva.E_iniciativa =  form.cleaned_data['E_iniciativa']
        eva.E_riesgo =  form.cleaned_data['E_riesgo']
        eva.E_estrategias = form.cleaned_data['E_estrategias']
        eva.E_seExpresa =  form.cleaned_data['E_seExpresa']
        #lenguaje y comunicacion
        eva.E_mencionaNombre =  form.cleaned_data['E_mencionaNombre']
        eva.E_mencionaDomicilio =  form.cleaned_data['E_mencionaDomicilio']
        eva.E_expresaSentir  =  form.cleaned_data['E_expresaSentir']
        eva.E_exprasaSentimientos =  form.cleaned_data['E_exprasaSentimientos']
        eva.E_recuerdaSusesos =  form.cleaned_data['E_recuerdaSusesos']
        eva.E_solicitaPalabra =  form.cleaned_data['E_solicitaPalabra']
        eva.E_respetaTurno =  form.cleaned_data['E_respetaTurno']
        eva.E_explica =  form.cleaned_data['E_explica']
        eva.E_formulaPreguntas =  form.cleaned_data['E_formulaPreguntas']
        eva.E_comprendeTareas =  form.cleaned_data['E_comprendeTareas']
        eva.E_solicitaAyuda = form.cleaned_data['E_solicitaAyuda']
        eva.E_conversa = form.cleaned_data['E_conversa']
        eva.E_expresaInformacion = form.cleaned_data['E_expresaInformacion']
        eva.E_escucha = form.cleaned_data['E_escucha']
        eva.E_narra = form.cleaned_data['E_narra']
        eva.E_creaCuentos = form.cleaned_data['E_creaCuentos']
        eva.E_memorizaPoemas = form.cleaned_data['E_memorizaPoemas']
        #Pensamiento matematico
        eva.E_realizaConteo =form.cleaned_data['E_realizaConteo']
        eva.E_reconoce = form.cleaned_data['E_reconoce']
        eva.E_plantea = form.cleaned_data['E_plantea']
        eva.E_sabeContar = form.cleaned_data['E_sabeContar']
        eva.E_sabeEscribir = form.cleaned_data['E_sabeEscribir']
        eva.E_izquierdaDerecha = form.cleaned_data['E_izquierdaDerecha']
        eva.E_arribaAbajo = form.cleaned_data['E_arribaAbajo']
        eva.E_llenoVacio = form.cleaned_data['E_llenoVacio']
        eva.E_conoceDiasMeses = form.cleaned_data['E_conoceDiasMeses']
        eva.E_ayerMañana = form.cleaned_data['E_ayerMañana']
        #Exploracion y conocimentos del mundo
        eva.E_describeSeresVivos = form.cleaned_data['E_describeSeresVivos']
        eva.E_identificaSeresVivos = form.cleaned_data['E_identificaSeresVivos']
        eva.E_describeFenomeno = form.cleaned_data['E_describeFenomeno']
        eva.E_clasifica = form.cleaned_data['E_clasifica']
        eva.E_SigueNormas = form.cleaned_data['E_SigueNormas']
        eva.E_manipula = form.cleaned_data['E_manipula']
        eva.E_pruebas = form.cleaned_data['E_pruebas']
        eva.E_reconoceExperimento = form.cleaned_data['E_reconoceExperimento']
        eva.E_expresaIdeas = form.cleaned_data['E_expresaIdeas']
        eva.E_establecePresePasa = form.cleaned_data['E_establecePresePasa']
        eva.E_comparteInformacion = form.cleaned_data['E_comparteInformacion']
        eva.E_identificaAmenazas = form.cleaned_data['E_identificaAmenazas']
        #expresion y apreciacion artistica
        eva.E_escuchaYCanta = form.cleaned_data['E_escuchaYCanta']
        eva.E_sigueRitmo = form.cleaned_data['E_sigueRitmo']
        eva.E_inventaCanciones = form.cleaned_data['E_inventaCanciones']
        eva.E_modifica = form.cleaned_data['E_modifica']
        eva.E_identificaDife = form.cleaned_data['E_identificaDife']
        eva.E_reproduceSecu = form.cleaned_data['E_reproduceSecu']
        eva.E_reconoceGeneroMu = form.cleaned_data['E_reconoceGeneroMu']
        eva.E_baila = form.cleaned_data['E_baila']
        eva.E_dramatizacion = form.cleaned_data['E_dramatizacion']
        eva.E_participa = form.cleaned_data['E_participa']
        eva.E_representa = form.cleaned_data['E_representa']
        eva.E_improvisa = form.cleaned_data['E_improvisa']
        eva.E_manipulaMateriales = form.cleaned_data['E_manipulaMateriales']
        eva.E_observaRe = form.cleaned_data['E_observaRe']
        eva.E_memorizaAutor = form.cleaned_data['E_memorizaAutor']
        #desarrollo fisico y salud
        eva.E_desplaza = form.cleaned_data['E_desplaza']
        eva.E_muestra = form.cleaned_data['E_muestra']
        eva.E_participaJuegos = form.cleaned_data['E_participaJuegos']
        eva.E_jalaEmpuja = form.cleaned_data['E_jalaEmpuja']
        eva.E_explora = form.cleaned_data['E_explora']
        eva.E_arma = form.cleaned_data['E_arma']
        eva.E_practica = form.cleaned_data['E_practica']
        eva.E_conocePractica = form.cleaned_data['E_conocePractica']
        eva.E_conocePropone = form.cleaned_data['E_conocePropone']
        eva.E_reconoceAmbien = form.cleaned_data['E_reconoceAmbien']
        eva.E_identificaPeligro = form.cleaned_data['E_identificaPeligro']
        eva.save()
        return super(EvaluarAlumno,self).form_valid(form)

class EvaDiario(FormView):
    template_name = "alumnos/evaluarDiario.html"
    form_class = Alumno_EvaDiario
    success_url = reverse_lazy('reporteDiario')

    def get_context_data(self, *args, **kwargs):
        ctx = super(EvaDiario, self).get_context_data(*args, **kwargs)
        #ctx['slug'] = self.kwargs['slug'] # or Tag.objects.get(slug=...)
        slug = self.kwargs['slug']
        ctx ['alumno'] = alumnos.objects.get(slug=slug)
        return ctx

    def form_valid(self, form):
        evaD = DiarioTrabajo()
        filtro = form.cleaned_data['DT_maestro']
        maes = Profesor.objects.get(pro_nombre=filtro)
        evaD.DT_maestro = maes
        filtroalum = form.cleaned_data['DT_alumno']
        slug = self.kwargs['slug']
        alu = alumnos.objects.get(slug=slug)
        evaD.DT_alumno = alu
        evaD.DT_fecha = form.cleaned_data['DT_fecha']
        evaD.DT_descripcion = form.cleaned_data['DT_descripcion']
        evaD.DT_actividadApoyo = form.cleaned_data['DT_actividadApoyo']
        evaD.DT_necesidades = form.cleaned_data['DT_necesidades']
        evaD.save()
        return super(EvaDiario,self).form_valid(form)

def detalleEvalSem(request, slug):
    eva = Evaluacion.objects.select_related().get(id = slug);
    ctx = {"Evaluacion": eva}
    return render(request, 'evaluaciones/detalleevaluacion.html', ctx)

def detalleDiario(request, slug):
    dia = DiarioTrabajo.objects.select_related().get(id = slug);
    ctx = {"Diario":dia}
    return render(request, 'alumnos/DetalleDiario.html', ctx)
