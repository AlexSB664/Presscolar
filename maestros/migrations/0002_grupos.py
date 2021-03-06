# Generated by Django 2.0.1 on 2018-02-28 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alumnos_alu_tutores'),
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gru_clave', models.CharField(max_length=10)),
                ('gru_alumnos', models.ManyToManyField(to='alumnos.alumnos')),
                ('gru_maestro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Maestro', to='maestros.maestros')),
            ],
        ),
    ]
