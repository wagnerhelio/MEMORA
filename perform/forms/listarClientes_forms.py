from django import forms

class ListarClienteForm(forms.Form):
    busca_nome = forms.CharField(
        label='Buscar por Nome',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do cliente'})
    )
