# Generated by Django 3.1.4 on 2021-01-05 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_article_hot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
