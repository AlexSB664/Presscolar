from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import maestros, User

class StudentSignUpForm(UserCreationForm):
    mae_apellidoPaterno = forms.CharField(label='Apellido Paterno')
    mae_apellidoMaterno = forms.CharField(label='Apellido Materno')
    mae_fechaNacimento = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.es_maes = True
        user.save()
        maes = maestros.objects.create(user=user)
        maes.mae_apellidoPaterno.add(*self.cleaned_data.get('mae_apellidoPaterno'))
        maes.mae_apellidoMaterno.add(*self.cleaned_data.get('mae_apellidoMaterno'))
        maes.mae_fechaNacimento.add(*self.cleaned_data.get('mae_fechaNacimento'))

        return user