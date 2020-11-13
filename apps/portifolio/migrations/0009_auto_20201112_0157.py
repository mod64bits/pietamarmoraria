# Generated by Django 3.1.2 on 2020-11-12 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0008_projeto_imagem_de_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem_de_capa',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='projetos_img/%Y/%m/%d/', verbose_name='Imagem de Capa'),
            preserve_default=False,
        ),
    ]
