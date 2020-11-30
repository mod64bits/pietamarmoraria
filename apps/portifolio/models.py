from django.db import models
from django.db.models import signals
from .signals import create_slug, imagem_pre_save


class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Categoria)


class Projeto(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao_curta = models.CharField('Descrição Curta', max_length=100, help_text='Descrição Curta para home')
    descricao = models.TextField('Descrição')
    categoria_projeto = models.ForeignKey(Categoria, name="Categoria", on_delete=models.PROTECT)
    home = models.BooleanField('Mostrar na Home?', default=True)
    imagem_de_capa = models.ImageField('Imagem de Capa', upload_to='projetos')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    mes = models.CharField('Mes', max_length=3, null=True, blank=True, editable=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Projeto)


def renomear_imagem(instance, filename):
    ext = filename.split('.')[-1]
    filename = ext
    img = 'portifolio/ag_{0}.{1}'.format(instance.nome, filename)

    return img


class Imagem(models.Model):
    nome = models.CharField('Nome', max_length=50)
    imagem = models.ImageField('Imagem', upload_to=renomear_imagem)
    projeto_portifolio = models.ForeignKey(Projeto, name='Projeto', on_delete=models.CASCADE)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.nome


signals.post_save.connect(imagem_pre_save, sender=Imagem)

