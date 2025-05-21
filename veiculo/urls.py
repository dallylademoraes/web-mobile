from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('pesquisar/', PesquisarVeiculoView.as_view(), name='pesquisar_veiculo'),
    path('novo/', CriarVeiculos.as_view(), name="criar-veiculo"),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
    path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('deletar/<int:pk>/', DeletarVeiculos.as_view(), name='deletar-veiculos')
]
