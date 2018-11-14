# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'机构名称')
    descs = models.TextField(verbose_name=u'机构描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = u'机构信息'
        verbose_name_plural = verbose_name


class Expert(models.Model):
    Organization = models.ForeignKey(Organization, verbose_name=u'所属机构')
    name = models.CharField(max_length=100, verbose_name=u'专家名称')
    descs = models.TextField(verbose_name=u'专家描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    filed = models.CharField(max_length=30, verbose_name='专业领域')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '专家信息'
        verbose_name_plural = verbose_name


class Couveuse(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'孵化器名字')
    area0 = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'所在地0')
    area1 = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'所在地1')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/incubator.png', max_length=100,verbose_name=u'主图')
    level = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'级别')
    url_introduce = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'介绍链接')
    url_companys = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'孵化企业链接')
    descs = models.TextField(blank=True, null=True, verbose_name=u'介绍')
    companys = models.TextField(blank=True, null=True, verbose_name=u'孵化企业')
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系人')
    contact_mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系电话')
    contact_email = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系邮箱')
    contact_post = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'邮编')
    addr = models.CharField(max_length=30, blank=True, null=True, verbose_name='地址')
    if_recommend = models.BooleanField(default=True, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = '孵化器库'
        verbose_name_plural = verbose_name


class Park(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'园区名字')
    area0 = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'所在地0')
    area1 = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'所在地1')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/incubator.png', max_length=100,verbose_name=u'主图')
    url_introduce = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'介绍链接')
    url_techservice = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'服务链接')
    descs = models.TextField(blank=True, null=True, verbose_name=u'介绍')
    techservice = models.TextField(blank=True, null=True, verbose_name=u'服务')
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系人')
    contact_mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系电话')
    contact_email = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系邮箱')
    contact_post = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'邮编')
    addr = models.CharField(max_length=30, blank=True, null=True, verbose_name='地址')
    if_recommend = models.BooleanField(default=True, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = '高新园区'
        verbose_name_plural = verbose_name


class Financial(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'金融机构名称')
    area0 = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'所在地0')
    area1 = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'所在地1')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/incubator.png', max_length=100,verbose_name=u'主图')
    url_introduce = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'介绍链接')
    url_services = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'服务链接')
    type = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'机构类型')
    descs = models.TextField(blank=True, null=True, verbose_name=u'介绍')
    services = models.TextField(blank=True, null=True, verbose_name=u'产品服务')
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系人')
    contact_mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系电话')
    contact_email = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'联系邮箱')
    contact_post = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'邮编')
    addr = models.CharField(max_length=30, blank=True, null=True, verbose_name='地址')
    if_recommend = models.BooleanField(default=True, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = '金融服务'
        verbose_name_plural = verbose_name
