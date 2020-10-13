from django import forms
from .models import Servico


class NovoServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
