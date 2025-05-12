from django import forms

class ListarFaturamentoForm(forms.Form):
    contrato = forms.CharField(required=False, label='Contrato')
    ano_referencia = forms.IntegerField(required=False, label='Ano')
