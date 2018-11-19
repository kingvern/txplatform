# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-16 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerproject',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_staff_set', to=settings.AUTH_USER_MODEL, verbose_name='\u4e1a\u52a1\u5458'),
        ),
        migrations.AlterField(
            model_name='buyerproject',
            name='step',
            field=models.CharField(choices=[('0', '\u7b49\u5f85\u652f\u4ed8\u5b9a\u91d1'), ('1', '\u5e73\u53f0\u5408\u540c\u7b7e\u8ba2'), ('2', '\u4e09\u65b9\u534f\u8bae\u7b7e\u8ba2'), ('3', '\u5c65\u7ea6\u5b8c\u6210'), ('-1', '\u53d6\u6d88\u6216\u7ec8\u6b62')], default='0', max_length=10, verbose_name='\u8ba2\u5355\u9636\u6bb5'),
        ),
    ]