# anuncio/urls.py
from django.urls import path
from anuncio.views import DetalhesAnuncio, ListarAnuncios

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('detalhes/<int:pk>/', DetalhesAnuncio.as_view(), name='detalhes-anuncio'),
]