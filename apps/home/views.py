from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, UpdateView
from django.views.generic.list import ListView
from .models import InformacoesSite

from core.alxiliarServicos import servicos_home
from apps.servicos.models import Servico
from ..banner.models import Banner


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = servicos_home()
        context['banners'] = Banner.objects.filter(ativo=True)
        return context


class EditarInformacoesDoSite(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InformacoesSite
    fields = '__all__'
    template_name = 'home/EditInfoSite.html'
    success_message = "Informações do Site Atualizados com Sucesso"


