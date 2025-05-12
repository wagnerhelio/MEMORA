from django.shortcuts import render, redirect, get_object_or_404
from perform.models import TipoFaturamento
from perform.forms.editarTipoFaturamento_forms import EditarTipoFaturamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_tipo_faturamento_view(request, id):
    tipo = get_object_or_404(TipoFaturamento, id=id)
    if request.method == 'POST':
        form = EditarTipoFaturamentoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_faturamento')
    else:
        form = EditarTipoFaturamentoForm(instance=tipo)
    return render(request, 'editar_tipo_faturamento.html', {'form': form})
