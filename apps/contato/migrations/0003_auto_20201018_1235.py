# Generated by Django 3.1.2 on 2020-10-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_auto_20201018_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='menssagem',
            new_name='mensagem',
        ),
    ]