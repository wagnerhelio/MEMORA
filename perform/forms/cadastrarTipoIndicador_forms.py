from django import forms
from perform.models import TipoIndicador

class CadastrarTipoIndicadorForm(forms.ModelForm):
    class Meta:
        model = TipoIndicador
        fields = ['codigo', 'descricao']
