from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import InformacoesSite
from core.envia_email import EnviaEmail

from core.alxiliarServicos import servicos_home
from apps.banner.models import Banner
from apps.contato.forms import NovoContatoForm


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


class ContatoSite(SuccessMessageMixin, CreateView):
    form_class = NovoContatoForm
    template_name = 'home/Contato.html'
    success_message = "%(nome)s"

    

    
    

    

