from django.db import models
from django.urls import reverse
from django.db.models import signals
from core.signals import create_slug
from apps.servicos.models import Categoria


class Banner(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    descricao = models.TextField('Descrição')
    categoria_banner = models.ForeignKey(Categoria, name='Categoria', on_delete=models.Case)
    ativo = models.BooleanField('Banner Ativo?', default=True)
    imagem = models.ImageField('Banner', null=True, blank=True, help_text='Escolha uma imagem de boa qualidade',  upload_to='banners')
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('banner:novo-banner')


signals.post_save.connect(create_slug, sender=Banner)
