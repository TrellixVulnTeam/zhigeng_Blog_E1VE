# Generated by Django 3.1.4 on 2021-01-05 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210105_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
    ]
