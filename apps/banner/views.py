from .models import Banner
from django.shortcuts import render
from django.views.generic import CreateView


class NovoBaner(CreateView):
    model = Banner
    fields = '__all__'
    template_name = 'banner/novo_banner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.filter(ativo=True)
        return context

