# Generated by Django 2.0.2 on 2018-03-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_auto_20180310_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='alu_foto',
            field=models.ImageField(null=True, upload_to='media/fotos'),
        ),
    ]
