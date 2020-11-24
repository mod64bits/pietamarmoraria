from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from .sinais import contato_signal


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    email = models.EmailField('Email')
    whatsapp = models.CharField('Whatsapp', max_length=100)
    mensagem = models.TextField('Mensagem')
    respondida = models.BooleanField('Respondido?', default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)



    def get_absolute_url(self):
        return reverse('home:contato')

    def __str__(self):
        return self.nome


post_save.connect(contato_signal, dispatch_uid=Contato)



