import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.ApiInstagram import PostInstagram
from core.envia_email import EnviaEmail
from django.template.defaultfilters import slugify


def contato_signal(sender, instance, signal, *args, **kwargs):
    # verifique se há id e atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        # obter informações de Slug
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        # salvar slug vazio
        if not getattr(instance, slug_name, None):
            # criar slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            # set slug
            setattr(instance, slug_name, slug)
            mensagem = f"Nome: {instance.nome}, Telefone: {instance.whatsapp}, Email: {instance.email}, " \
                       f"Mensagem: {instance.mensagem}"
            enviar = EnviaEmail(mensagem)
            enviar.rementente_mensagem()
            instance.save()
