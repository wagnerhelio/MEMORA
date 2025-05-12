from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from perform.models import Faturamento
from perform.forms.listarFaturamento_forms import ListarFaturamentoForm

@login_required
def listar_faturamento_view(request):
    form = ListarFaturamentoForm(request.GET or None)
    faturamentos = Faturamento.objects.all()

    if form.is_valid():
        ano = form.cleaned_data.get('ano_referencia')
        if ano:
            faturamentos = faturamentos.filter(ano_referencia=ano)

    return render(request, 'listar_faturamento.html', {
        'form': form,
        'faturamentos': faturamentos
    })
