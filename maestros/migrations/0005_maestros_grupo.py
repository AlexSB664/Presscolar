# Generated by Django 2.0.2 on 2018-04-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0004_auto_20180305_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='maestros',
            name='grupo',
            field=models.CharField(default='maestro', max_length=100),
        ),
    ]
