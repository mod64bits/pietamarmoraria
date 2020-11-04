# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify

def retorna_mes(numero):
    nome_mes = ['jan', 'fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    return nome_mes[numero -1]


def create_slug(sender, instance, signal, *args, **kwargs):

    # verifique se há id e atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        # obter informações de Slug
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        # salvar slug vazio

        if not getattr(instance, slug_name, None):
            instance.mes = retorna_mes(instance.created.month)
            # criar slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            # set slug
            setattr(instance, slug_name, slug)
            # save instance
            instance.save()


def imagem_pre_save(signal, instance, sender, **kwargs):
    """Este signal renomeia a imagem"""
    novo_nome = f"pieta_{instance.imagem}"
    instance.imagem = novo_nome


