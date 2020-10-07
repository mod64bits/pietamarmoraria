from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from .models import InformacoesSite


class Home(TemplateView):
    template_name = 'home/home.html'


class EditarInformacoesDoSite(SuccessMessageMixin, UpdateView):
    model = InformacoesSite
    fields = '__all__'
    template_name = 'home/EditInfoSite.html'
    success_message = "Informações do Site Atualizados com Sucesso"
