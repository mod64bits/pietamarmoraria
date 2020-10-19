from django import forms
from .models import Contato


class NovoContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['respondida']
