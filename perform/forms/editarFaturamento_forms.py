from django import forms
from perform.models import Faturamento

class EditarFaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = '__all__'
