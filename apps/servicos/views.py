from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, TemplateView
from .models import Categoria
from .forms import NovoServicoForm
from core.alxiliarServicos import todas_categoria, todos_servicos
from .models import Servico


class NovaCategoria(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'servico/NovaCategoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = todas_categoria()
        return context


class EditarCategoria(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'servico/EditarCategoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = todas_categoria()
        return context


class NovoServico(CreateView):
    form_class = NovoServicoForm
    template_name = 'servico/NovoServico.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servivos'] = todos_servicos()
        return context


class EditarServico(UpdateView):
    model = Servico
    fields = '__all__'
    template_name = 'servico/EditarServico.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servivos'] = todos_servicos()
        return context


class TodosServicos(ListView):
    model = Servico
    context_object_name = 'servicos_lista'
    template_name = 'home/TodosServicos.html'

    def get_context_data(self, **kwargs):
        servicos_lista = super().get_context_data(**kwargs)
        # servicos_lista['categorias'] = todas_categoria()
        return servicos_lista


def categoria(request, nome):
    categoria = Categoria.objects.get(nome=nome)
    context = {
        'categoria_atual': categoria,
        'servicos_list': Servico.objects.filter(categoria=categoria)
    }
    return render(request, 'home/CategoriaServico.html', context)
