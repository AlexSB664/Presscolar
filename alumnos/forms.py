from django import forms
from alumnos.models import alumnos

#class Alumno_Form(forms.ModelForm):
#	
#	model = alumnos
#	field = "__all__"
class Alumno_Form(forms.ModelForm):
	class Meta:
		model = alumnos
		fields = "__all__"
        
        #widgets = {
        #    'alu_nombre' = forms.TextInput(attrs = {'class': 'form-control'})
        #}