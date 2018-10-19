# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-19 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0003_auto_20181019_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='agency',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4ee3\u7406\u673a\u6784'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='agent',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4ee3\u7406\u4eba'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='applicant',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7533\u8bf7\u4eba'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8054\u7cfb\u4eba'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='contact_mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='\u4e13\u5229\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='hire',
            field=models.IntegerField(default=0, verbose_name='\u4f63\u91d1'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='inventor',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u53d1\u660e\u4eba'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='main_pic',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u4e13\u5229\u4e3b\u56fe'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='more_pic',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m', verbose_name='\u4e13\u5229\u56fe'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='price',
            field=models.IntegerField(default=0, verbose_name='\u4ef7\u683c'),
        ),
    ]
