from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
import datetime


class StudentSignUpForm(UserCreationForm):#forms.Form UserCreationForm
    nombres = forms.CharField(label='Nombres:', widget=forms.TextInput(attrs={'class':'form-control', 'required': 'True'}))
    paterno = forms.CharField(label='Apellido Paterno:', widget=forms.TextInput(attrs={'class':'form-control','required' : 'True'}))
    materno = forms.CharField(label='Apellido Materno:', widget=forms.TextInput(attrs={'class':'form-control','required' : 'True'}))
    nacimiento = forms.CharField(label='Fecha de nacimiento:',initial=datetime.date.today, widget=forms.TextInput(attrs={'type':'date'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
        
        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control'}),
            'password1': forms.PasswordInput(attrs = {'class' : 'form-control'}),
        }
        
        labels = {
            'username' : 'Usuario:',
            'password1': 'Contraseña',
        }