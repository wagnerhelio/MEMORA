from django import forms

class ExcluirClienteForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este cliente")
