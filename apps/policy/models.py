# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'行政名称')

    class Meta:
        verbose_name = u'省份'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Department(models.Model):
    Province = models.ForeignKey(Province, verbose_name=u'所属行政')
    name = models.CharField(max_length=100, verbose_name=u'部门名称')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Policy(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'政策名')
    Province = models.ForeignKey(Province, verbose_name=u'所属行政')
    Department = models.ForeignKey(Department, verbose_name=u'所属部门')
    detail = models.TextField(verbose_name=u'政策详情')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '政策信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'咨讯名')
    detail = models.TextField(verbose_name=u'咨讯详情')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '咨询信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Chart(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'图表名')
    data = models.TextField(verbose_name=u'图表数据')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '图表信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name