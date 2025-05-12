from django import forms

class ListarTipoFaturamentoForm(forms.Form):
    nome = forms.CharField(label="Nome", required=False)
