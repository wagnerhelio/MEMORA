from django.shortcuts import render, redirect, get_object_or_404
from perform.models import TipoIndicador
from perform.forms.editarTipoIndicador_forms import EditarTipoIndicadorForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_tipo_indicador_view(request, id):
    indicador = get_object_or_404(TipoIndicador, id=id)
    if request.method == 'POST':
        form = EditarTipoIndicadorForm(request.POST, instance=indicador)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_indicador')
    else:
        form = EditarTipoIndicadorForm(instance=indicador)
    return render(request, 'editar_tipo_indicador.html', {'form': form})
