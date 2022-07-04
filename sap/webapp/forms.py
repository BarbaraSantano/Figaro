from django.forms import ModelForm, EmailInput

from webapp.models import Alumnos


class AlumnosForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
        widgets = {
            'email_alumnos': EmailInput(attrs={'type':'email'})
        }