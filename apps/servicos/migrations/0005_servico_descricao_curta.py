# Generated by Django 3.1.2 on 2020-11-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_auto_20201014_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='descricao_curta',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição Curta'),
        ),
    ]