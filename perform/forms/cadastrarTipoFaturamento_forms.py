from django import forms
from perform.models import TipoFaturamento

class CadastrarTipoFaturamentoForm(forms.ModelForm):
    class Meta:
        model = TipoFaturamento
        fields = ['nome']
