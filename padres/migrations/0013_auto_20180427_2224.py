# Generated by Django 2.0.1 on 2018-04-27 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padres', '0012_auto_20180427_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='pro_apellidoMaterno',
            field=models.CharField(default='s', max_length=70),
        ),
        migrations.AddField(
            model_name='profesor',
            name='pro_apellidoPaterno',
            field=models.CharField(default='s', max_length=70),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='pro_fechaNacimento',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
