from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from perform.models import Faturamento
from perform.forms.excluirFaturamento_forms import ExcluirFaturamentoForm

@login_required
def excluir_faturamento_view(request, id):
    faturamento = get_object_or_404(Faturamento, id=id)
    if request.method == 'POST':
        form = ExcluirFaturamentoForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmar']:
            faturamento.delete()
            return redirect('listar_faturamento')
    else:
        form = ExcluirFaturamentoForm()
    return render(request, 'excluir_faturamento.html', {'form': form, 'faturamento': faturamento})
