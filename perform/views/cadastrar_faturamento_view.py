from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from perform.forms.cadastrarFaturamento_forms import CadastrarFaturamentoForm

@login_required
def cadastrar_faturamento_view(request):
    if request.method == 'POST':
        form = CadastrarFaturamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_faturamento')
    else:
        form = CadastrarFaturamentoForm()
    return render(request, 'cadastrar_faturamento.html', {'form': form})
