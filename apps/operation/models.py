# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from patent.models import Patent
from project.models import Project


# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    policy_name = models.CharField(max_length=50, verbose_name=u'专利名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'其他慢慢加')), default=1,
                                   verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class BuyerPatent(models.Model):
    buyer = models.ForeignKey(UserProfile, verbose_name=u'买家')
    order_name = models.CharField(max_length=100, default='', verbose_name=u'单位名称')
    order_address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    order_contact = models.CharField(max_length=100, default='', verbose_name=u'联系人')
    order_mobile = models.CharField(max_length=11, default='', verbose_name=u'手机')
    patent = models.ForeignKey(Patent, verbose_name=u'专利')
    base_price = models.IntegerField(default=0, verbose_name=u'基础费')
    serve_fee = models.IntegerField(default=0, verbose_name=u'服务费')
    total_price = models.IntegerField(default=0, verbose_name=u'总费')
    step = models.CharField(max_length=10, default='0', choices=(('0', u'未付款'), ('1', u'已付款'), ('2', u'已提交专利局')),
                            verbose_name=u'订单阶段')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'专利交易管理'
        verbose_name_plural = verbose_name


class BuyerProject(models.Model):
    buyer = models.ForeignKey(UserProfile, verbose_name=u'买家')
    project = models.ForeignKey(Project, verbose_name=u'项目')
    step = models.CharField(max_length=10, default='0', choices=(('0', u'未付款'), ('1', u'已付款'), ('2', u'已提交专利局')),
                            verbose_name=u'合作阶段')
    contract = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"合同",
        default='',
        max_length=100)
    protocol = models.FileField(
        upload_to="protocol/resource/%Y/%m",
        verbose_name=u"协议",
        default='',
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'项目转换管理'
        verbose_name_plural = verbose_name
