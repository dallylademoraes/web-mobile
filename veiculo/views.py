from django.http import FileResponse, Http404
from django.shortcuts import render
from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from veiculo.serializers import SerializadorVeiculo
from rest_framework.authentication import TokenAuthentication
#from django.contrib.auth.mixins import LoginRequiredMixin

class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()

class ListarVeiculos(ListView): # LoginRequiredMixin
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

class CriarVeiculos(CreateView): # LoginRequiredMixin, 
    """
    View para a criação de novos veiculos
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto nõa encontrada ou acesso não autorizado!")
        except Exception as exception:
            raise exception

class EditarVeiculos(UpdateView): #LoginRequiredMixin
    """
    View para a edição de veiculos já cadastrados.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(DeleteView): #LoginRequiredMixin
    """
    View para a exclusão de veiculos.
    """
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

