from django.shortcuts import render, redirect
from perform.forms.cadastrarTipoFaturamento_forms import CadastrarTipoFaturamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_tipo_faturamento_view(request):
    if request.method == 'POST':
        form = CadastrarTipoFaturamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_faturamento')
    else:
        form = CadastrarTipoFaturamentoForm()
    return render(request, 'cadastrar_tipo_faturamento.html', {'form': form})
