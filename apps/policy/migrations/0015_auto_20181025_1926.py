# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-25 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0014_auto_20181025_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': '\u884c\u653f\u7ea7\u522b', 'verbose_name_plural': '\u884c\u653f\u7ea7\u522b'},
        ),
        migrations.AddField(
            model_name='province',
            name='main',
            field=models.CharField(choices=[('0', '\u4e2d\u592e'), ('1', '\u5317\u4eac'), ('2', '\u5929\u6d25'), ('3', '\u6cb3\u5317\u7701')], default='0', max_length=100, null=True, verbose_name='\u4e0a\u7ea7\u540d\u79f0'),
        ),
    ]
