from django.contrib import admin
from .models import Categoria, Servico


@admin.register(Categoria)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created')


@admin.register(Servico)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'created')
