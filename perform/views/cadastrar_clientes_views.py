from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from perform.forms import CadastrarClienteForm

@login_required
def cadastrar_clientes_view(request):
    if request.method == 'POST':
        form = CadastrarClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = CadastrarClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})