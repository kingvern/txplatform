# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-22 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0006_auto_20181022_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='tab',
            field=models.CharField(default='', max_length=20, verbose_name='\u4e3b\u83dc\u5355'),
        ),
        migrations.AddField(
            model_name='chart',
            name='tab2',
            field=models.CharField(default='', max_length=20, verbose_name='\u5206\u83dc\u5355'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='data',
            field=models.TextField(default='', verbose_name='\u56fe\u8868\u6570\u636e'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='\u56fe\u8868\u540d'),
        ),
    ]