from django.db import models
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from django.db.models import signals

from core.signals import create_slug


class Categoria(models.Model):
    nome = models.SlugField('Nome', max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('servicos:nova-categoria')


signals.post_save.connect(create_slug, sender=Categoria)


class Servico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao_curta = models.TextField('Descrição Curta', null=True, blank=True)
    descricao = models.TextField('Descrição')
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    mostra_na_home = models.BooleanField('Mostra na Pagina Inicial?', default=True)
    imagem = models.ImageField('Imagem', null=True, blank=True, upload_to='servicos')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        img = Image.open(self.imagem)
        output_size = (870, 500)

        img.thumbnail(output_size)
        img = img.convert('RGB')
        output = BytesIO()
        img.save(output, format='JPEG', qualit=100)
        output.seek(0)

        self.imagem = InMemoryUploadedFile(output, 'ImagemField', f'{self.imagem.name.split(".")[0]}.jpg', 'image/jpg',
                                           sys.getsizeof(output), None)
        super(Servico, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('servicos:novo-servico')


signals.post_save.connect(create_slug, sender=Servico)


