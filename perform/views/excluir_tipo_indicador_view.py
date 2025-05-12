from django.shortcuts import render, redirect, get_object_or_404
from perform.models import TipoIndicador
from perform.forms.excluirTipoIndicador_forms import ExcluirTipoIndicadorForm
from django.contrib.auth.decorators import login_required

@login_required
def excluir_tipo_indicador_view(request, id):
    indicador = get_object_or_404(TipoIndicador, id=id)
    if request.method == 'POST':
        form = ExcluirTipoIndicadorForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmar']:
            indicador.delete()
            return redirect('listar_tipo_indicador')
    else:
        form = ExcluirTipoIndicadorForm()
    return render(request, 'excluir_tipo_indicador.html', {'form': form, 'indicador': indicador})
