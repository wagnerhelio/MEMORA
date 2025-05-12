from django.shortcuts import render
from perform.models import TipoFaturamento
from perform.forms.listarTipoFaturamento_forms import ListarTipoFaturamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_tipo_faturamento_view(request):
    form = ListarTipoFaturamentoForm(request.GET or None)
    tipos = TipoFaturamento.objects.all()
    if form.is_valid() and form.cleaned_data.get('nome'):
        tipos = tipos.filter(nome__icontains=form.cleaned_data['nome'])
    return render(request, 'listar_tipo_faturamento.html', {'form': form, 'tipos': tipos})
