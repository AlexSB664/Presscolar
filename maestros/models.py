from django.db import models
from alumnos.models import alumnos
from padres.models import Profesor
from django.db.models.manager import EmptyManager


class grupos(models.Model):
    gru_clave = models.CharField(max_length = 10)
    gru_maestro = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=True, null=True, related_name="Maestro")
    gru_alumnos = models.ManyToManyField(alumnos)
    gru_salon = models.CharField(max_length = 10, default='')
    gru_grado = models.IntegerField(null=True)
    
    def __str__(self):
        return self.gru_clave
        
    
class DiarioTrabajo(models.Model):
    DT_maestro = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    DT_alumno = models.ForeignKey(alumnos, on_delete= models.CASCADE)
    DT_fecha = models.DateField(auto_now_add = True)
    DT_descripcion = models.TextField()
    DT_actividadApoyo = models.TextField()
    DT_necesidades = models.TextField()
    
    def __str__(self):
        return str(self.DT_alumno)
    
class Evaluacion(models.Model):
    E_maestro = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    E_alumno = models.ForeignKey(alumnos, on_delete = models.CASCADE)
    E_fecha = models.DateField(auto_now_add=True)
    #Desarrollo personal y social
    E_comparte = models.IntegerField(null=True)
    E_apoya = models.IntegerField(null=True)
    E_pregunta = models.IntegerField(null=True)
    E_sugerencia = models.IntegerField(null=True)
    E_controla = models.IntegerField(null=True)
    E_cuida = models.IntegerField(null=True)
    E_espera = models.IntegerField(null=True)
    E_negocia = models.IntegerField(null=True)
    E_trabajaEquipo = models.IntegerField(null=True)
    E_respeta = models.IntegerField(null=True)
    E_cuidadoso = models.IntegerField(null=True)
    E_involucra = models.IntegerField(null=True)
    E_iniciativa = models.IntegerField(null=True)
    E_riesgo = models.IntegerField(null=True)
    E_estrategias= models.IntegerField(null=True)
    E_seExpresa = models.IntegerField(null=True)
    #lenguaje y comunicacion 
    E_mencionaNombre = models.IntegerField(null=True)
    E_mencionaDomicilio = models.IntegerField(null=True)
    E_expresaSentir  = models.IntegerField(null=True)
    E_exprasaSentimientos = models.IntegerField(null=True)
    E_recuerdaSusesos = models.IntegerField(null=True)
    E_solicitaPalabra = models.IntegerField(null=True)
    E_respetaTurno = models.IntegerField(null=True)
    E_explica = models.IntegerField(null=True)
    E_formulaPreguntas = models.IntegerField(null=True)
    E_comprendeTareas = models.IntegerField(null=True)
    E_solicitaAyuda = models.IntegerField(null=True)
    E_conversa = models.IntegerField(null=True)
    E_expresaInformacion = models.IntegerField(null=True)
    E_escucha = models.IntegerField(null=True)
    E_narra = models.IntegerField(null=True)
    E_creaCuentos = models.IntegerField(null=True)
    E_memorizaPoemas = models.IntegerField(null=True)
    #pensamiento matematico
    E_realizaConteo = models.IntegerField(null=True)
    E_reconoce = models.IntegerField(null=True)
    E_plantea = models.IntegerField(null=True)
    E_sabeContar = models.IntegerField(null=True)
    E_sabeEscribir = models.IntegerField(null=True)
    E_izquierdaDerecha = models.IntegerField(null=True)
    E_arribaAbajo = models.IntegerField(null=True)
    E_llenoVacio = models.IntegerField(null=True)
    E_conoceDiasMeses = models.IntegerField(null=True)
    E_ayerMañana = models.IntegerField(null=True)
    #exploracion y conocimiento del mundo
    E_describeSeresVivos = models.IntegerField(null=True)
    E_identificaSeresVivos = models.IntegerField(null=True)
    E_describeFenomeno = models.IntegerField(null=True)
    E_clasifica = models.IntegerField(null=True)
    E_SigueNormas = models.IntegerField(null=True)
    E_manipula = models.IntegerField(null=True)
    E_pruebas = models.IntegerField(null=True)
    E_reconoceExperimento = models.IntegerField(null=True)
    E_expresaIdeas = models.IntegerField(null=True)
    E_establecePresePasa = models.IntegerField(null=True)
    E_comparteInformacion = models.IntegerField(null=True)
    E_identificaAmenazas = models.IntegerField(null=True)
    #expresion y apreciacion artistica
    E_escuchaYCanta = models.IntegerField(null=True)
    E_sigueRitmo = models.IntegerField(null=True)
    E_inventaCanciones = models.IntegerField(null=True)
    E_modifica = models.IntegerField(null=True)
    E_identificaDife = models.IntegerField(null=True)
    E_reproduceSecu = models.IntegerField(null=True)
    E_reconoceGeneroMu = models.IntegerField(null=True)
    E_baila = models.IntegerField(null=True)
    E_dramatizacion = models.IntegerField(null=True)
    E_participa = models.IntegerField(null=True)
    E_representa = models.IntegerField(null=True)
    E_improvisa = models.IntegerField(null=True)
    E_manipulaMateriales = models.IntegerField(null=True)
    E_observaRe = models.IntegerField(null=True)
    E_memorizaAutor = models.IntegerField(null=True)
    #desarollo fisico y salud 
    E_desplaza = models.IntegerField(null=True)
    E_muestra = models.IntegerField(null=True)
    E_participaJuegos = models.IntegerField(null=True)
    E_jalaEmpuja = models.IntegerField(null=True)
    E_explora = models.IntegerField(null=True)
    E_construye = models.IntegerField(null=True)
    E_arma = models.IntegerField(null=True)
    E_practica = models.IntegerField(null=True)
    E_conocePractica = models.IntegerField(null=True)
    E_conocePropone = models.IntegerField(null=True)
    E_reconoceAmbien = models.IntegerField(null=True)
    E_identificaPeligro = models.IntegerField(null=True)



