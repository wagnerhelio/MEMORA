from django.shortcuts import render, redirect
from perform.forms.cadastrarTipoIndicador_forms import CadastrarTipoIndicadorForm
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_tipo_indicador_view(request):
    if request.method == 'POST':
        form = CadastrarTipoIndicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_indicador')
    else:
        form = CadastrarTipoIndicadorForm()
    return render(request, 'cadastrar_tipo_indicador.html', {'form': form})
