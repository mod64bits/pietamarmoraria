# Generated by Django 3.1.2 on 2020-10-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_servico_mostra_na_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
    ]
