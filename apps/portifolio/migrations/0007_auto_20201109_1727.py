# Generated by Django 3.1.2 on 2020-11-09 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0006_projeto_mes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagem',
            options={'verbose_name_plural': 'Imagens'},
        ),
        migrations.RenameField(
            model_name='imagem',
            old_name='Categoria',
            new_name='Projeto',
        ),
    ]
