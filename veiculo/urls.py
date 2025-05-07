from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('pesquisar/', PesquisarVeiculoView.as_view(), name='pesquisar_veiculo'),
]
