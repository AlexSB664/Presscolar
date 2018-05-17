# Generated by Django 2.0.2 on 2018-05-16 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padres', '0013_auto_20180427_2224'),
        ('alumnos', '0012_alumnos_slug'),
        ('maestros', '0007_auto_20180430_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_fecha', models.DateField(auto_now_add=True)),
                ('E_comparte', models.IntegerField(null=True)),
                ('E_apoya', models.IntegerField(null=True)),
                ('E_pregunta', models.IntegerField(null=True)),
                ('E_sugerencia', models.IntegerField(null=True)),
                ('E_controla', models.IntegerField(null=True)),
                ('E_cuida', models.IntegerField(null=True)),
                ('E_espera', models.IntegerField(null=True)),
                ('E_negocia', models.IntegerField(null=True)),
                ('E_trabajaEquipo', models.IntegerField(null=True)),
                ('E_respeta', models.IntegerField(null=True)),
                ('E_cuidadoso', models.IntegerField(null=True)),
                ('E_involucra', models.IntegerField(null=True)),
                ('E_iniciativa', models.IntegerField(null=True)),
                ('E_riesgo', models.IntegerField(null=True)),
                ('E_estrategias', models.IntegerField(null=True)),
                ('E_seExpresa', models.IntegerField(null=True)),
                ('E_mencionaNombre', models.IntegerField(null=True)),
                ('E_mencionaDomicilio', models.IntegerField(null=True)),
                ('E_expresaSentir', models.IntegerField(null=True)),
                ('E_exprasaSentimientos', models.IntegerField(null=True)),
                ('E_recuerdaSusesos', models.IntegerField(null=True)),
                ('E_solicitaPalabra', models.IntegerField(null=True)),
                ('E_respetaTurno', models.IntegerField(null=True)),
                ('E_explica', models.IntegerField(null=True)),
                ('E_formulaPreguntas', models.IntegerField(null=True)),
                ('E_comprendeTareas', models.IntegerField(null=True)),
                ('E_solicitaAyuda', models.IntegerField(null=True)),
                ('E_conversa', models.IntegerField(null=True)),
                ('E_expresaInformacion', models.IntegerField(null=True)),
                ('E_escucha', models.IntegerField(null=True)),
                ('E_narra', models.IntegerField(null=True)),
                ('E_creaCuentos', models.IntegerField(null=True)),
                ('E_memorizaPoemas', models.IntegerField(null=True)),
                ('E_realizaConteo', models.IntegerField(null=True)),
                ('E_reconoce', models.IntegerField(null=True)),
                ('E_plantea', models.IntegerField(null=True)),
                ('E_sabeContar', models.IntegerField(null=True)),
                ('E_sabeEscribir', models.IntegerField(null=True)),
                ('E_izquierdaDerecha', models.IntegerField(null=True)),
                ('E_arribaAbajo', models.IntegerField(null=True)),
                ('E_llenoVacio', models.IntegerField(null=True)),
                ('E_conoceDiasMeses', models.IntegerField(null=True)),
                ('E_ayerMañana', models.IntegerField(null=True)),
                ('E_describeSeresVivos', models.IntegerField(null=True)),
                ('E_identificaSeresVivos', models.IntegerField(null=True)),
                ('E_describeFenomeno', models.IntegerField(null=True)),
                ('E_clasifica', models.IntegerField(null=True)),
                ('E_SigueNormas', models.IntegerField(null=True)),
                ('E_manipula', models.IntegerField(null=True)),
                ('E_pruebas', models.IntegerField(null=True)),
                ('E_reconoceExperimento', models.IntegerField(null=True)),
                ('E_expresaIdeas', models.IntegerField(null=True)),
                ('E_establecePresePasa', models.IntegerField(null=True)),
                ('E_comparteInformacion', models.IntegerField(null=True)),
                ('E_identificaAmenazas', models.IntegerField(null=True)),
                ('E_escuchaYCanta', models.IntegerField(null=True)),
                ('E_sigueRitmo', models.IntegerField(null=True)),
                ('E_inventaCanciones', models.IntegerField(null=True)),
                ('E_modifica', models.IntegerField(null=True)),
                ('E_identificaDife', models.IntegerField(null=True)),
                ('E_reproduceSecu', models.IntegerField(null=True)),
                ('E_reconoceGeneroMu', models.IntegerField(null=True)),
                ('E_baila', models.IntegerField(null=True)),
                ('E_dramatizacion', models.IntegerField(null=True)),
                ('E_participa', models.IntegerField(null=True)),
                ('E_representa', models.IntegerField(null=True)),
                ('E_improvisa', models.IntegerField(null=True)),
                ('E_manipulaMateriales', models.IntegerField(null=True)),
                ('E_observaRe', models.IntegerField(null=True)),
                ('E_memorizaAutor', models.IntegerField(null=True)),
                ('E_desplaza', models.IntegerField(null=True)),
                ('E_muestra', models.IntegerField(null=True)),
                ('E_participaJuegos', models.IntegerField(null=True)),
                ('E_jalaEmpuja', models.IntegerField(null=True)),
                ('E_explora', models.IntegerField(null=True)),
                ('E_construye', models.IntegerField(null=True)),
                ('E_arma', models.IntegerField(null=True)),
                ('E_practica', models.IntegerField(null=True)),
                ('E_conocePractica', models.IntegerField(null=True)),
                ('E_conocePropone', models.IntegerField(null=True)),
                ('E_reconoceAmbien', models.IntegerField(null=True)),
                ('E_identificaPeligro', models.IntegerField(null=True)),
                ('E_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumnos')),
                ('E_maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padres.Profesor')),
            ],
        ),
        migrations.AlterField(
            model_name='diariotrabajo',
            name='DT_actividadApoyo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='diariotrabajo',
            name='DT_descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='diariotrabajo',
            name='DT_necesidades',
            field=models.TextField(),
        ),
    ]
