# Generated by Django 3.1.2 on 2020-10-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_auto_20201013_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.SlugField(unique=True, verbose_name='Nome'),
        ),
    ]