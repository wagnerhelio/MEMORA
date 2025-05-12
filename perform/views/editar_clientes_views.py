from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from perform.models import Cliente
from perform.forms import EditarClienteForm

@login_required
def editar_clientes_view(request, cliente_id):
    cliente  = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = EditarClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = EditarClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})
