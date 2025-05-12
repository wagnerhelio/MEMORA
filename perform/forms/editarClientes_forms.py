from django import forms
from perform.models import Cliente

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cnpj',
            'data_inicio_contrato',
            'data_fim_contrato',
            'data_fim_adendo',
            'previsibilidade_operacional',
            'meta_contrato',
        ]
        widgets = {
            'data_inicio_contrato': forms.DateInput(attrs={'type': 'date'}),
            'data_fim_contrato': forms.DateInput(attrs={'type': 'date'}),
            'data_fim_adendo': forms.DateInput(attrs={'type': 'date'}),
        }
