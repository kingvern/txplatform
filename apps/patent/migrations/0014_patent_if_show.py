# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-14 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0013_auto_20181114_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='patent',
            name='if_show',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
    ]
