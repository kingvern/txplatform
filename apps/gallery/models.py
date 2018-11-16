# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class Gallery(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'活动名字')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/incubator.png', max_length=100, verbose_name=u'主图')
    descs = UEditorField(verbose_name=u"详情", width=600, height=300, imagePath="patent/ueditor/",
                         filePath="patent/ueditor/", default='')
    addr = models.CharField(max_length=30, blank=True, null=True, verbose_name='地址')
    time_begin = models.DateTimeField(default=datetime.now, verbose_name=u'活动开始日期')
    time_end = models.DateTimeField(default=datetime.now, verbose_name=u'活动结束日期')
    status = models.CharField(max_length=50, verbose_name=u'活动状态')
    type = models.CharField(max_length=10, default='0',
                            choices=(('0', u'线上活动'), ('1', u'线下活动')), verbose_name=u'活动类型')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    join_num = models.IntegerField(default=0, verbose_name=u'报名人数')
    if_recommend = models.BooleanField(default=True, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = '展会平台'
        verbose_name_plural = verbose_name
