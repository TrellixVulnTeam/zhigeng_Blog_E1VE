# Generated by Django 3.1.4 on 2021-01-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('sex', models.IntegerField(blank=True, choices=[(1, '男'), (2, '女'), (0, '未知')], default='男', verbose_name='性别')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('qq_name', models.CharField(blank=True, default='null', max_length=128, verbose_name='QQ账号')),
                ('wc_name', models.CharField(blank=True, default='null', max_length=128, verbose_name='微信账号')),
                ('phone', models.CharField(blank=True, default='null', max_length=128, verbose_name='电话')),
                ('email', models.EmailField(blank=True, default='null', max_length=254, verbose_name='Email')),
                ('signature', models.CharField(default='null', max_length=128, verbose_name='签名')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '读者信息',
                'verbose_name_plural': '读者信息',
            },
        ),
    ]
