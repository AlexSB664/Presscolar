# Generated by Django 2.0.1 on 2018-05-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0016_merge_20180520_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='alu_genero',
            field=models.CharField(default='Masculino', max_length=10),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='slug',
            field=models.SlugField(default='KGB073JBN54K1XB3X7L0NTJL', max_length=24),
        ),
    ]
