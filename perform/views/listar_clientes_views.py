from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from perform.models import Cliente
from perform.forms import ListarClienteForm

@login_required
def listar_clientes_view(request):
    form = ListarClienteForm(request.GET or None)
    clientes = Cliente.objects.all()

    if form.is_valid() and form.cleaned_data.get('busca_nome'):
        clientes = clientes.filter(nome__icontains=form.cleaned_data['busca_nome'])

    return render(request, 'listar_clientes.html', {
        'form': form,
        'clientes': clientes
    })
