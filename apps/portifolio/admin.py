from django.contrib import admin
from .models import Categoria, Imagem, Projeto


class ProjetoImagens(admin.TabularInline):
    model = Imagem

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created', 'modified')


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'created', 'modified')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    inlines = [ProjetoImagens]
    list_display = ('nome', 'descricao_curta', 'slug', 'created', 'modified')


