from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from perform.models import Cliente

@login_required
def excluir_clientes_view(request, cliente_id):
    veiculo = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_cleintes')

    return render(request, 'excluir_clientes.html', {'cliente': cliente})
