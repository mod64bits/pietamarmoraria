from apps.servicos.models import Categoria, Servico


def todas_categoria():
    cat = Categoria.objects.all()
    return cat


def todos_servicos():
    serv = Servico.objects.all()
    return serv


def servicos_home():
    serv = Servico.objects.filter(mostra_na_home=True).order_by('-created')
    return serv
