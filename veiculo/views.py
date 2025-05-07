from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import ListView

class ListarVeiculos(ListView):
    """
    View para listar veículos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'


class PesquisarVeiculoView(ListView):
    """
    View para pesquisar veículos pelo modelo.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'  # Usa o mesmo template da listagem

    def get_queryset(self):
        termo = self.request.GET.get('q')
        if termo:
            return Veiculo.objects.filter(modelo__icontains=termo)
        return Veiculo.objects.all()
