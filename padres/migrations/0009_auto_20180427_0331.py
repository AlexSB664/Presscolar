# Generated by Django 2.0.1 on 2018-04-27 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('padres', '0008_auto_20180427_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'permissions': (('is_tutor', 'Is_Tutor'), ('is_teacher', 'Is_Teacher'))},
        ),
    ]
