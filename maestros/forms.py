from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import maestros, User

class StudentSignUpForm(UserCreationForm):
    paterno = forms.CharField(label='Apellido Paterno:', widget=forms.TextInput(attrs={'class':'form-control'}))
    materno = forms.CharField(label='Apellido Materno:', widget=forms.TextInput(attrs={'class':'form-control'}))
    nacimiento = forms.CharField(label='Fecha de nacimiento:', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
    
    
    
    

class AltaMaestros(forms.ModelForm):
    
    class Meta:
        model = maestros
        fields = '__all__'
        
        
        #paterno = forms.CharField()
        #materno = forms.CharField()
        #nacimiento = forms.CharField()
        
        widgets = {
            #'mae_nombre': forms.ModelChoiceField(queryset=  ,attrs={'class': 'form-control'}),
            'mae_apellidoMaterno' : forms.TextInput(attrs={'class':'form-control'}),
            'mae_apellidoPaterno' : forms.TextInput(attrs={'class': 'form-control'}),
            'mae_fechaNacimento': forms.TextInput(attrs={'class' : 'form-control', 'type': 'date'})
        }
        
        labels = {
            'mae_nombre': 'Usuario',
            'mae_apellidoMaterno': 'Apellido paterno',
            'mae_apellidoPaterno': 'Apellido materno',
            'mae_fechaNacimento': 'Fecha de nacimiento',
        }
                            