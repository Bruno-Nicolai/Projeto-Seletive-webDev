# Generated by Django 4.1.3 on 2022-11-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_vagas_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
