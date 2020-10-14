from django.urls import path
from apps.servicos.views import NovaCategoria, NovoServico, EditarServico, EditarCategoria

app_name = 'servicos'

urlpatterns = [
    path('nova/categoria/', NovaCategoria.as_view(), name='nova-categoria'),
    path('editar/categoria/<slug:slug>/', EditarCategoria.as_view(), name='editar_categoria'),
    path('novo/servico/', NovoServico.as_view(), name='novo-servico'),
    path('editar/servico/<slug:slug>/', EditarServico.as_view(), name='editar_servico'),
]
