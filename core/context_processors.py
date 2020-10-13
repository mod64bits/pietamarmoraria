from apps.home.models import InformacoesSite
from apps.servicos.models import Categoria


def site_infor(request):
    info = InformacoesSite.objects.filter(id=1)
    SITEINFO = {}
    for i in info:
        SITEINFO['nome'] = i.nome
        SITEINFO['email'] = i.email
        SITEINFO['telefone'] = i.telefone
        SITEINFO['endereco'] = i.endereco
        SITEINFO['sobre'] = i.sobre
        SITEINFO['img_sobre'] = i.img_sobre
        SITEINFO['logo'] = i.logo
        SITEINFO['facebook'] = i.facebook
        SITEINFO['instagram'] = i.instagram
        SITEINFO['twitter'] = i.twitter

    return SITEINFO


def categorias(request):
    return {
        'categorias': Categoria.objects.all()
    }
