from django.shortcuts import render

# Create your views here.
from veiculo.models import Veiculo
from django.views.generic import ListView

class ListarVeiculos(ListView):
  """
  View para listar veículos cadastrados.
  """
  model = Veiculo
  context_object_name = 'veiculos'
  template_name = 'veiculo/listar.html'