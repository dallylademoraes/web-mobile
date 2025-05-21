# anuncio/views.py
from django.views.generic import ListView, DetailView
from veiculo.models import Veiculo

class ListarAnuncios(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/anuncio.html'
    def get_queryset(self):
        return Veiculo.objects.all().order_by('-ano')

class DetalhesAnuncio(DetailView):
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculo/detalhes.html'