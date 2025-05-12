from django.shortcuts import render
from perform.models import TipoIndicador
from perform.forms.listarTipoIndicador_forms import ListarTipoIndicadorForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_tipo_indicador_view(request):
    form = ListarTipoIndicadorForm(request.GET or None)
    indicadores = TipoIndicador.objects.all()
    if form.is_valid() and form.cleaned_data.get('descricao'):
        indicadores = indicadores.filter(descricao__icontains=form.cleaned_data['descricao'])
    return render(request, 'listar_tipo_indicador.html', {'form': form, 'indicadores': indicadores})
