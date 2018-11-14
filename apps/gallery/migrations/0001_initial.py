# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-14 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6d3b\u52a8\u540d\u5b57')),
                ('pic', models.ImageField(default='image/incubator.png', upload_to='image/%Y/%m', verbose_name='\u4e3b\u56fe')),
                ('descs', models.TextField(blank=True, null=True, verbose_name='\u4ecb\u7ecd')),
                ('addr', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5730\u5740')),
                ('time_begin', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6d3b\u52a8\u5f00\u59cb\u65e5\u671f')),
                ('time_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6d3b\u52a8\u7ed3\u675f\u65e5\u671f')),
                ('status', models.CharField(max_length=50, verbose_name='\u6d3b\u52a8\u72b6\u6001')),
                ('type', models.CharField(choices=[('0', '\u7ebf\u4e0a\u6d3b\u52a8'), ('1', '\u7ebf\u4e0b\u6d3b\u52a8')], default='0', max_length=10, verbose_name='\u6d3b\u52a8\u7c7b\u578b')),
                ('if_recommend', models.BooleanField(default=True, verbose_name='\u662f\u5426\u63a8\u8350')),
            ],
            options={
                'verbose_name': '\u5c55\u4f1a\u5e73\u53f0',
                'verbose_name_plural': '\u5c55\u4f1a\u5e73\u53f0',
            },
        ),
    ]
