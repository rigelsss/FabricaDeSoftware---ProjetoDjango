from django import forms
from .models import Autor, Detalhe

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'ies']

class DetalheForm(forms.ModelForm):
    class Meta:
        model = Detalhe
        fields = ['cidade', 'autor', 'cep']
