import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from core.ApiInstagram import PostInstagram


from apps.servicos.models import Servico


@receiver(post_save, sender=Servico)
def postar_servico_instagram(sender, instance, **kwargs):
    PostInstagram(username="mod64bits", password="Mikita*271982", imagem=instance.imagem, description=instance.descricao)

