# Generated by Django 3.1.2 on 2020-11-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_auto_20201128_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True, unique=True),
        ),
    ]