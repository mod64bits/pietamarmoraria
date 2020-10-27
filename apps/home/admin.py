from django.contrib import admin
from .models import InformacoesSite


@admin.register(InformacoesSite)
class InformacoesSiteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone',  'endereco', 'sobre', 'facebook', 'instagram')
