# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-14 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0011_auto_20181114_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='patent',
            name='note',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5ba1\u6838\u610f\u89c1'),
        ),
    ]