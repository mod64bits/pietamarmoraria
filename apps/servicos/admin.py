from django.contrib import admin
from .models import Categoria, Servico, ImagemServico


class ImagemServicoAdmin(admin.TabularInline):
    model = ImagemServico

@admin.register(Categoria)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created')


@admin.register(Servico)
class BannerAdmin(admin.ModelAdmin):
    inlines = [ImagemServicoAdmin]
    list_display = ('nome', 'descricao', 'created')

@admin.register(ImagemServico)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'created', 'modified')


