# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-01 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181019_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='\u9a8c\u8bc1\u7801')),
                ('mobile', models.CharField(max_length=50, verbose_name='\u624b\u673a\u53f7')),
                ('send_type', models.CharField(choices=[('register', '\u6ce8\u518c'), ('reset_pwd', '\u5fd8\u8bb0\u5bc6\u7801')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '\u624b\u673a\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u624b\u673a\u9a8c\u8bc1\u7801',
            },
        ),
    ]