from django.urls import path
from apps.home.views import Home, EditarInformacoesDoSite

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('edit/site/<int:pk>/', EditarInformacoesDoSite.as_view(), name='edit_informacoes_site'),
]
