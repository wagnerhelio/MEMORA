from django import forms
from perform.models import TipoFaturamento

class EditarTipoFaturamentoForm(forms.ModelForm):
    class Meta:
        model = TipoFaturamento
        fields = ['nome']
