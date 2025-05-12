from django.shortcuts import render, redirect, get_object_or_404
from perform.models import TipoFaturamento
from perform.forms.excluirTipoFaturamento_forms import ExcluirTipoFaturamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def excluir_tipo_faturamento_view(request, id):
    tipo = get_object_or_404(TipoFaturamento, id=id)
    if request.method == 'POST':
        form = ExcluirTipoFaturamentoForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmar']:
            tipo.delete()
            return redirect('listar_tipo_faturamento')
    else:
        form = ExcluirTipoFaturamentoForm()
    return render(request, 'excluir_tipo_faturamento.html', {'form': form, 'tipo': tipo})
