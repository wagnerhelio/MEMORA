from django import forms

class ExcluirTipoIndicadorForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este tipo de indicador.")
