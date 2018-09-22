# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = u'机构信息'
        verbose_name_plural = verbose_name


class Expert(models.Model):
    Organization = models.ForeignKey(Organization, verbose_name=u'所属类别')
    name = models.CharField(max_length=100, verbose_name=u'专家名称')
    desc = models.TextField(verbose_name=u'专家描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    filed = models.CharField(max_length=30, verbose_name='专业领域')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '专家信息'
        verbose_name_plural = verbose_name
