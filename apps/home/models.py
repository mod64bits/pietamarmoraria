from django.db import models
from django.urls import reverse



class InformacoesSite(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=30)
    endereco = models.TextField('Endereço', null=True, blank=True)
    sobre = models.TextField('Resumo da Empresa')
    img_sobre = models.ImageField('Imagem Sobre', null=True, blank=True, upload_to='infoSite')
    logo = models.ImageField('Logo', null=True, blank=True, upload_to='infoSite')
    facebook = models.URLField('FaceBook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    



    def get_absolute_url(self):
        return reverse('home:edit_informacoes_site', kwargs={'pk': self.pk})


