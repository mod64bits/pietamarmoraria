from django.core.mail import send_mail


class EnviaEmail:
    def __init__(self, menssagem):
        self.menssagem = menssagem

    def rementente_mensagem(self):
        send_mail(
            "Contato do Site",
            self.menssagem,
            'contato@pietamarmoraria.ind.br',
            ['pieta@pietamarmoraria.ind.br'],
            fail_silently=False,
        )
