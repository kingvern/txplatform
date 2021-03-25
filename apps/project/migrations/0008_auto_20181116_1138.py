# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-16 11:38
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='if_show',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='project',
            name='note',
            field=models.CharField(blank=True, default='1', max_length=20, null=True, verbose_name='\u5ba1\u6838\u610f\u89c1'),
        ),
        migrations.AddField(
            model_name='project',
            name='shop_status',
            field=models.CharField(choices=[('-1', '\u5df2\u4e0b\u67b6'), ('0', '\u5ba1\u6838\u4e2d'), ('1', '\u5df2\u4e0a\u67b6'), ('2', '\u5df2\u4ea4\u6613')], default='1', max_length=20, verbose_name='\u4e0a\u67b6\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cooperation',
            field=models.CharField(choices=[('0', '\u80a1\u6743\u6295\u8d44'), ('1', '\u6280\u672f\u8f6c\u8ba9'), ('2', '\u8bb8\u53ef\u4f7f\u7528'), ('3', '\u5408\u4f5c\u5f00\u53d1'), ('4', '\u5408\u4f5c\u5174\u529e\u65b0\u4f01\u4e1a'), ('5', '\u5176\u4ed6')], default='0', max_length=100, verbose_name='\u5408\u4f5c\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_step',
            field=models.CharField(choices=[('0', '\u672a\u77e5'), ('1', '\u5b9e\u9a8c\u5ba4\u9636\u6bb5'), ('2', '\u6837\u54c1\u9636\u6bb5'), ('3', '\u5c0f\u8bd5\u9636\u6bb5'), ('4', '\u4e2d\u8bd5\u9636\u6bb5'), ('5', '\u91cf\u4ea7\u9636\u6bb5')], default='0', max_length=100, verbose_name='\u6210\u719f\u5ea6'),
        ),
    ]