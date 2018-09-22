# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'专利类别')

    class Meta:
        verbose_name = u'专利类别'
        verbose_name_plural = verbose_name


class Patent(models.Model):
    Category = models.ForeignKey(Category, verbose_name=u'所属类别')
    name = models.CharField(max_length=100, verbose_name=u'专利名')
    detail = models.TextField(verbose_name=u'专利详情')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '专利信息'
        verbose_name_plural = verbose_name
