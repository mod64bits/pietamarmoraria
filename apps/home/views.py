from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView
from django.views.generic.list import ListView
from .models import InformacoesSite
from apps.portifolio.models import Projeto
from apps.servicos.models import Servico
from core.alxiliarServicos import servicos_home
from apps.banner.models import Banner
from apps.contato.forms import NovoContatoForm


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = servicos_home()
        context['banners'] = Banner.objects.filter(ativo=True)
        context['projetos'] = Projeto.objects.filter(home=True)
        return context


class EditarInformacoesDoSite(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InformacoesSite
    fields = '__all__'
    template_name = 'home/EditInfoSite.html'
    success_message = "Informações do Site Atualizados com Sucesso"


class ContatoSite(SuccessMessageMixin, CreateView):
    form_class = NovoContatoForm
    template_name = 'home/Contato.html'
    success_message = "%(nome)s"






class ProjetosList(ListView):
    model = Projeto
    context_object_name = 'todos_projetos'
    template_name = 'home/ListaDeProjetos.html'


class ProjetoDetalhe(DetailView):
    model = Projeto
    template_name = 'home/ProjetoDetalhe.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class ServicoDetalhe(DetailView):
    model = Servico
    template_name = 'home/ServicoDetalhe.html'

