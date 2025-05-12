from django import forms

class ExcluirFaturamentoForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este registro de faturamento.")
