# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-14 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='fav_num',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6b21\u6570'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='join_num',
            field=models.IntegerField(default=0, verbose_name='\u62a5\u540d\u4eba\u6570'),
        ),
    ]
