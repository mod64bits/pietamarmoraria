# Generated by Django 3.1.2 on 2020-11-12 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0007_auto_20201109_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='projetos_img/%Y/%m/%d/',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem de Capa'),
        ),
    ]