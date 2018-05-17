from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User


class StudentSignUpForm(UserCreationForm):#forms.Form UserCreationForm
    paterno = forms.CharField(label='Apellido Paterno:', widget=forms.TextInput(attrs={'class':'form-control','required' : 'True'}))
    materno = forms.CharField(label='Apellido Materno:', widget=forms.TextInput(attrs={'class':'form-control','required' : 'True'}))
    nacimiento = forms.CharField(label='Fecha de nacimiento:', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))    