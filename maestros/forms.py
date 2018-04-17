from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import maestros, User

class StudentSignUpForm(UserCreationForm):
    mae_apellidoPaterno = forms.CharField(label='Apellido Paterno')
    mae_apellidoMaterno = forms.CharField(label='Apellido Materno')
    mae_fechaNacimento = forms.DateField()

#    labels = {
#        'mae_apellidoPaterno' :'Apellido paterno :',
#        'mae_apellidoMaterno' : 'Apellido materno :',
#        'mae_fechaNacimento': 'Fecha de nacimiento :'
#    }
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.es_maes = True
        user.save()
        maes = maestros()
        maes.mae_nombre = user
        maes.mae_apellidoPaterno  = (self.cleaned_data.get('mae_apellidoPaterno'))
        maes.mae_apellidoMaterno =(self.cleaned_data.get('mae_apellidoMaterno'))
        maes.mae_fechaNacimento = self.cleaned_data.get('mae_fechaNacimento')
        maes.save()
        
        return user
    
    
    

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
            'mae_apellidoMaterno': 'Apellido paterno: ',
            'mae_apellidoPaterno': 'Apellido materno: ',
            'mae_fechaNacimiento': 'Fecha de nacimiento',
        }
                            