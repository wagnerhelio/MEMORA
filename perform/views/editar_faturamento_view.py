from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from perform.models import Faturamento
from perform.forms.editarFaturamento_forms import EditarFaturamentoForm

@login_required
def editar_faturamento_view(request, id):
    faturamento = get_object_or_404(Faturamento, id=id)
    if request.method == 'POST':
        form = EditarFaturamentoForm(request.POST, instance=faturamento)
        if form.is_valid():
            form.save()
            return redirect('listar_faturamento')
    else:
        form = EditarFaturamentoForm(instance=faturamento)
    return render(request, 'editar_faturamento.html', {'form': form})
