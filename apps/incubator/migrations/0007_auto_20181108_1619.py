# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-08 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0006_remove_park_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='couveuse',
            name='pic',
            field=models.ImageField(default='image/incubator.png', upload_to='image/%Y/%m', verbose_name='\u4e3b\u56fe'),
        ),
        migrations.AddField(
            model_name='financial',
            name='pic',
            field=models.ImageField(default='image/incubator.png', upload_to='image/%Y/%m', verbose_name='\u4e3b\u56fe'),
        ),
        migrations.AddField(
            model_name='park',
            name='pic',
            field=models.ImageField(default='image/incubator.png', upload_to='image/%Y/%m', verbose_name='\u4e3b\u56fe'),
        ),
    ]
