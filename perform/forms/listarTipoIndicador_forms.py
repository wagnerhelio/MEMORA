from django import forms

class ListarTipoIndicadorForm(forms.Form):
    descricao = forms.CharField(label="Descrição", required=False)
