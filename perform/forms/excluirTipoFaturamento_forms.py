from django import forms

class ExcluirTipoFaturamentoForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este tipo de faturamento.")
