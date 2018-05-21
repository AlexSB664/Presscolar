from django import forms
from alumnos.models import alumnos
from padres.models import Tutor
import datetime

#class Alumno_Form(forms.ModelForm):
#	
#	model = alumnos
#	field = "__all__"
class Alumno_Form(forms.ModelForm):
	class Meta:
		model = alumnos
		fields = "__all__"
        
        #widgets = {
        #    'alu_nombre' = forms.TextInput(attrs = {'class': 'form-control'})
        #}
class Alumno_Chido(forms.Form):
	alu_nombre = forms.CharField(label='Nombres:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	alu_genero = forms.CharField(label='Genero:', widget=forms.TextInput(attrs={'class':'form-control'}))
	alu_tutores = forms.ModelMultipleChoiceField(queryset=Tutor.objects.all(),label='Tutores:')
	alu_vigente = forms.BooleanField(label='Vigente:', widget=forms.TextInput(attrs={'class':'form-control'}))
	alu_fechaIngreso = forms.DateField(label='Fecha de Ingreso:',initial=datetime.date.today, widget=forms.TextInput(attrs={'type':'date'}))
	alu_observaciones = forms.CharField(label='Observaciones:', widget=forms.TextInput(attrs={'class':'form-control'}))
	slug = forms.CharField(label='Slug:', widget=forms.TextInput(attrs={'class': 'form-control'}))

class Alumno_Eva(forms.Form):
	E_maestro = forms.CharField(label='Maestro:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	E_alumno = forms.CharField(label='Alumno:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	E_fecha = forms.DateField(label='Fecha de evaluacion:',initial=datetime.date.today, widget=forms.TextInput(attrs={'type':'date','readonly':'readonly'}))
	E_comparte = forms.IntegerField(label='Comparte libremente detalles cotidianos de su casa, escuela, comunidad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3','min':'1','max':'3'}))
	E_apoya =  forms.CharField(label='Apoya a los demás dando sugerencias para lograr realizarlo:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3','min':'1','max':'3'}))
	E_pregunta =  forms.CharField(label='Realiza preguntas para dar solución a su curiosidad o duda:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3','min':'1','max':'3'}))
	E_sugerencia =  forms.CharField(label='Acepta sugerencias en las actividades que lo requiere:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_controla =  forms.CharField(label='Controla coductas impulsivas de agresión fisica o verbales a sus compañeros:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_cuida =  forms.CharField(label='Cuida su persona de no lastimarse:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_espera =  forms.CharField(label='Espera su turno para intervenir, comparte materiales en las actividades:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_negocia =  forms.CharField(label='Negocia, argumenta las formas de trabajar las actividades con sus compañeros:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_trabajaEquipo =  forms.CharField(label='Trabaja en equipo:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_respeta =  forms.CharField(label='Respeta normas para la convivencia dentro y fuera del salón:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_cuidadoso =  forms.CharField(label='Es cuidadoso con sus pertenencias:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_involucra =  forms.CharField(label='Se involucra activamente en las actividades colectivas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_iniciativa =  forms.CharField(label='Tiene iniciativa al realizar las actividades dentro y fuera del aula:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_riesgo =  forms.CharField(label='Reconoce situaciones de riesgo:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_estrategias=  forms.CharField(label='Propone soluciones o estrategias para la solucionar algún conflicto o problema:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_seExpresa =  forms.CharField(label='Expresa sobre cómo se siente:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	#lenguaje y comunicacion
	E_mencionaNombre =  forms.CharField(label='Menciona sus nombres completos y los de su familia:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_mencionaDomicilio =  forms.CharField(label='Menciyona sus datos de domicilio , teléfono y señas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_expresaSentir  =  forms.CharField(label='Expresa y comparte lo que provoca alegría, tristeza, temor asombro:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_exprasaSentimientos =  forms.CharField(label='Da a conocer lo que le agrada-disgusta, acuerdos y desacuerdos de algo (juegos, canciones, actividades):', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_recuerdaSusesos =  forms.CharField(label='Recuerda sucesos y los da a conocer a los demás:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_solicitaPalabra =  forms.CharField(label='Solicita la palabra:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_respetaTurno =  forms.CharField(label='Respeta turnos de habla de los demás:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_explica =  forms.CharField(label='Explica las indicaciones a seguir en las actividades:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_formulaPreguntas =  forms.CharField(label='Formula preguntas e instrucciones realizar actividades:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_comprendeTareas =  forms.CharField(label='Comprende las indicaciones para realizar las actividades o tareas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_solicitaAyuda = forms.CharField(label='Solicita ayuda cuando no puede realizar las actividades o tareas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_conversa = forms.CharField(label='Conversa con sus compañeros sobre un tema cada vez más prolongadas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_expresaInformacion = forms.CharField(label='Expresa información sobre un tema:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_escucha = forms.CharField(label='Escucha narraciones, cuentos, relatos, leyendas y expresa su opinión sobre lo que escucho:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_narra = forms.CharField(label='Narra cuentos, relatos, leyendas utilizando entonacion y el volumen de voz:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_creaCuentos = forms.CharField(label='Crea cuentos, canciones, rimas, trabalenguas, adivinanzas y chistes:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_memorizaPoemas = forms.CharField(label='Memoriza poemas, canciones, rondas, adivinanzas, trabalenguas y chistes:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	#Pensamiento matematico
	E_realizaConteo = forms.CharField(label='Realiza actividades de conteo orden estable, cordialidad, correspondencia uno a uno y abstracción:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_reconoce = forms.CharField(label='Reconoce y nombra objetos (figuras geométricas):', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_plantea = forms.CharField(label='Plantea y resuelve problemas en situaciones que le son familiares como agregar, quitar igualar, comprar y repartir objetos:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_sabeContar = forms.CharField(label='Sabe contar hasta el numero 100:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_sabeEscribir = forms.CharField(label='Sabe escribir hasta el numero 100:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_izquierdaDerecha = forms.CharField(label='Ubica izquierda y derecha:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_arribaAbajo = forms.CharField(label='Ubica arriba, abajo, enfrente, atrás, cercas, lejos, alto, bajo , grande, pequeño:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_llenoVacio = forms.CharField(label='Ubica lleno, vacio, corto, largo, pesado y ligero:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_conoceDiasMeses = forms.CharField(label='Conoce días, meses y los recuerda con facilidad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_ayerMañana = forms.CharField(label='Reconoce el ayer, mañana y pasado:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	#Exploracion y conocimentos del mundo
	E_describeSeresVivos = forms.CharField(label='Describe las características de los elementos y de los seres vivos:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_identificaSeresVivos = forms.CharField(label='Identidica algunos rasgos de los seres vivos:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_describeFenomeno = forms.CharField(label='Describe lo que observa mientras ocurre un fenómeno natural:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_clasifica = forms.CharField(label='Clasifica elementos y seres de la naturaleza según sus características como animales que habitan en el mar, tierra, cielo, animales mamíferos, etc:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_SigueNormas = forms.CharField(label='Sigue normas de seguridad de utilizar materiales, herramientas e instrumentos:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_manipula = forms.CharField(label='Manipula objetos a su alcance como tierra, lodo y arena:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_pruebas = forms.CharField(label='Realiza pruebas y mezclaz de elementos (experimentos):', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_reconoceExperimento = forms.CharField(label='Reconoce y describe cambios que ocurren durante y después de algún experimento:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_expresaIdeas = forms.CharField(label='Expresa con sus propias ideas iniciales con las finalidad y las modifica consecuencia de experiencia:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_establecePresePasa = forms.CharField(label='Establece relación entre el presente y el pasado:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_comparteInformacion = forms.CharField(label='Comparte información de las costumbres de su familia y su cominidad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_identificaAmenazas = forms.CharField(label='Identifica semejanzas y direncia entre su cultura familiar y las de sus compañeros:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	#expresion y apreciacion artistica
	E_escuchaYCanta = forms.CharField(label='Escucha y canta canciones:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_sigueRitmo = forms.CharField(label='Sigue el ritmo de canciones:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_inventaCanciones = forms.CharField(label='Inventa canciones conocidas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_modifica = forms.CharField(label='Modifica el ritmo de canciones conocidas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_identificaDife = forms.CharField(label='Identifica diferentes fuentes sonoras como la naturaleza, canto de aves, de animales y instrumentos:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_reproduceSecu = forms.CharField(label='Reproduce secuencias ritmicas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_reconoceGeneroMu = forms.CharField(label='Reconoce distintos géneros de música:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_baila = forms.CharField(label='Baila libremente al escuchar música:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_dramatizacion = forms.CharField(label='Realiza dramatización de cuentos, de situaciones de la vida cotidiana:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_participa = forms.CharField(label='Participa en actividades de expresión corporal movimiento de animales objetos y personas:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_representa = forms.CharField(label='Representa mediante la expresion corporal desplazándose en espacios fuera y dentro del aula:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_improvisa = forms.CharField(label='Improvisa movimientos al escuchar una canción:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_manipulaMateriales = forms.CharField(label='Manipula distintos materiales plásticos y crea pinturas, dibujos, grabado :', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_observaRe = forms.CharField(label='Observan y reflexiona obras de distintos  tiempos y culturas y conserva sobre detalles que llaman su atencion y por que:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_memorizaAutor = forms.CharField(label='Memoriza e identifica el nombre del autor de algunas de las obras de arte conocida:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	#desarrollo fisico y salud
	E_desplaza = forms.CharField(label='Se desplaza en diferentes direcciones trepando, rodando y deslizándose:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_muestra = forms.CharField(label='Muestra control y equilibrio de los juegos como subirse, bajarse, trepar y colgarse:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_participaJuegos = forms.CharField(label='Participa en juegos donde implica permanecer quieto, en distancias, en velocidad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_jalaEmpuja = forms.CharField(label='Jala, empuja y captura objetos en movimiento:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_explora = forms.CharField(label='Explora, manipula, elige objetos, instrumentos y herramientas de trabajo y sabe que pueden hacer y en donde:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_arma = forms.CharField(label='Arma rompecabezas de distinto grado de dificultad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_practica = forms.CharField(label='Práctica medidas de seguridad y evita ponerse en peligro:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_conocePractica = forms.CharField(label='Conoce, practica y propone algunas medidas para evitar enfermedades:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_conocePropone = forms.CharField(label='Contruye o modela objetos de su propia creación:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_reconoceAmbien = forms.CharField(label='Reconoce algunos problemas ambientales y sus repercusiones:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))
	E_identificaPeligro = forms.CharField(label='Identidica que hace ren caso de peligro a su persona, a la familia o a la comunidad:', widget=forms.TextInput(attrs={'type':'number','min':'1','max':'3'}))

class Alumno_EvaDiario(forms.Form):
	DT_maestro = forms.CharField(label='Maestro:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	DT_alumno = forms.CharField(label='Alumno:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	DT_fecha = forms.DateField(label='Fecha de evaluacion:',initial=datetime.date.today, widget=forms.TextInput(attrs={'type':'date','readonly':'readonly'}))
	DT_descripcion = forms.CharField(label='Descripcion:', widget=forms.TextInput(attrs={'class':'form-control'}))
	DT_actividadApoyo = forms.CharField(label='Actividad de apoyo:', widget=forms.TextInput(attrs={'class':'form-control'}))
	DT_necesidades = forms.CharField(label='Necesidades:', widget=forms.TextInput(attrs={'class':'form-control'}))	