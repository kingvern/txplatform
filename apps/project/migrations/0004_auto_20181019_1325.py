# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-19 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181019_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_category',
            new_name='project_step',
        ),
    ]