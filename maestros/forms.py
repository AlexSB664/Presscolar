from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class StudentSignUpForm(UserCreationForm):
    paterno = forms.CharField(label='Apellido Paterno:', widget=forms.TextInput(attrs={'class':'form-control'}))
    materno = forms.CharField(label='Apellido Materno:', widget=forms.TextInput(attrs={'class':'form-control'}))
    nacimiento = forms.CharField(label='Fecha de nacimiento:', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
                   