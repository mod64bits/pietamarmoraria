from django.urls import path
from apps.home.views import Home, EditarInformacoesDoSite
from apps.servicos.views import TodosServicos, categoria
from .views import ContatoSite, ProjetosList


app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projetos/', ProjetosList.as_view(), name='projetos'),
    path('contato/', ContatoSite.as_view(), name='contato'),
    path('servicos/', TodosServicos.as_view(), name='todos_servicos'),
    path('categoria/<str:nome>/', categoria, name='categoria_servico'),
    path('edit/site/<int:pk>/', EditarInformacoesDoSite.as_view(), name='edit_informacoes_site'),
]
