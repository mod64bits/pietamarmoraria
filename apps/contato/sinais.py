from django.core.mail import send_mail
from django.template.defaultfilters import slugify


def contato_signal(sender, instance, signal, *args, **kwargs):
    # verifique se há id e atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        # obter informações de Slug
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        # salvar slug vazio
        if not getattr(instance, slug_name, None):
            # criar slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            # set slug
            setattr(instance, slug_name, slug)
            nome = instance.nome
            mensagem = instance.mensagem
            email = instance.email
            whatsapp = instance.whatsapp

            send_mail(
                'contato do site',
                f'Novo Contato Realizado no site de {nome}, email {email}, whatsapp {whatsapp}, mensagem: {mensagem}',
                'contato@agmarmoraria.ind.br',
                ['ag@agmarmoraria.ind.br'],
                fail_silently=False,
            )

            instance.save()
