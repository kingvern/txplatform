# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-23 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='Organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incubator.Organization', verbose_name='\u6240\u5c5e\u673a\u6784'),
        ),
    ]
