from django.urls import path
from apps.home.views import Home, EditarInformacoesDoSite
from apps.servicos.views import TodosServicos, categoria

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('servicos/', TodosServicos.as_view(), name='todos_servicos'),
    path('categoria/<str:nome>/', categoria, name='categoria_servico'),
    path('edit/site/<int:pk>/', EditarInformacoesDoSite.as_view(), name='edit_informacoes_site'),
]
