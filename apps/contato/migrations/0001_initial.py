# Generated by Django 3.1.2 on 2020-10-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('whatsapp', models.CharField(max_length=100, verbose_name='Whatsapp')),
                ('messagem', models.TextField(verbose_name='Mensagem')),
                ('respondida', models.BooleanField(default=False, verbose_name='Respondido?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
    ]
