# Generated by Django 3.1.2 on 2020-10-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_banner_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(blank=True, help_text='Escolha uma imagem de boa qualidade', null=True, upload_to='banners', verbose_name='Banner'),
        ),
    ]