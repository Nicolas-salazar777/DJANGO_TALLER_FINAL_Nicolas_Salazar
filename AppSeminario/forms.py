from django import forms
from AppSeminario.models import Inscritos

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'
    
