# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'行政名称')
    main = models.CharField(max_length=100, choices=(('0', u'中央'), ('1', u'北京'), ('2', '天津'), ('3', '河北省')),
                            default='0', null=True,verbose_name=u'上级名称')
    if_show = models.BooleanField(default=True, verbose_name=u'是否显示')

    class Meta:
        verbose_name = u'行政级别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'部门名称')
    if_show = models.BooleanField(default=True, verbose_name=u'是否显示')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Policy(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name=u'政策名')
    policy_id = models.CharField(max_length=20, default='', verbose_name=u'政策ID')
    addr = models.ForeignKey(Province,on_delete=models.CASCADE,  verbose_name=u'所属行政')
    source = models.ForeignKey(Department,on_delete=models.CASCADE,  verbose_name=u'所属部门')
    info = models.TextField(verbose_name=u'政策详情')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    pubDate = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '政策信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'资讯名')
    detail = models.TextField(verbose_name=u'资讯详情')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    if_toutiao = models.BooleanField(default=False, verbose_name=u'是否是头条')
    if_show = models.BooleanField(default=False, verbose_name=u'是否显示')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100,
                            verbose_name=u'主图')
    pubDate = models.DateTimeField(default=datetime.now, verbose_name=u'发布日期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '平台新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Chart(models.Model):
    tab = models.CharField(default='', max_length=20, verbose_name='主菜单')
    tab2 = models.CharField(default='', max_length=20, verbose_name='分菜单')
    title = models.CharField(default='', max_length=100, verbose_name=u'图表名')
    data = models.TextField(default='', verbose_name=u'图表数据')
    type = models.CharField(default='pie', choices=(
        ('pie', u'饼状图'), ('bar', u'柱状图'), ('bar2', u'横向柱状图'), ('line', u'折线图'), ('map', u'地图')), max_length=100,
                            verbose_name=u'图表类型')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '图表信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
