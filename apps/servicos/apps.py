from django.apps import AppConfig


class ServicosConfig(AppConfig):
    name = 'apps.servicos'

    def ready(self):
        import apps.servicos.sinais

