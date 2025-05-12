from django import forms
from perform.models import Faturamento

class CadastrarFaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = [
            'contrato',
            'indicador',
            'ano_referencia',
            'valor_jan',
            'valor_fev',
            'valor_mar',
            'valor_abr',
            'valor_mai',
            'valor_jun',
            'valor_jul',
            'valor_ago',
            'valor_set',
            'valor_out',
            'valor_nov',
            'valor_dez',
        ]
