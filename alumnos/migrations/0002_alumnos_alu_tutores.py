# Generated by Django 2.0.1 on 2018-02-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padres', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='alu_tutores',
            field=models.ManyToManyField(null=True, to='padres.Tutor'),
        ),
    ]
