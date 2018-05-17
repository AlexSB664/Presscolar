from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddTutorForm(UserCreationForm):
    fname = forms.CharField(label='Nombres:', widget=forms.TextInput(attrs={'class':'form-control'}))
    lname = forms.CharField(label='Apellido paterno:',widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidoM = forms.CharField(label='Apellido materno:', widget=forms.TextInput(attrs={'class':'form-control'}))
    parent = forms.CharField(label='Parentesco:', widget=forms.TextInput(attrs={'class':'form-control'}))
    descrip = forms.CharField(label='Descripcion:', widget=forms.TextInput(attrs={'class':'form-control'}))
    domicilio = forms.CharField(label='Domicilio:',widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(label='Telefono:', widget=forms.TextInput(attrs={'type':'number', 'class':'form-control'}))
#    password1=forms.CharField(label='Contrasena:',forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#    password2=forms.CharField(label='Confirmar contrasena:',forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    
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