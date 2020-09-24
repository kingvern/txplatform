# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

from users.models import UserProfile


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'头条名', default='')
    pic = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100,
                            verbose_name=u'头条主图')
    detail = UEditorField(verbose_name=u"详情", width=600, height=300, imagePath="project/ueditor/",
                          filePath="club/ueditor/", default='')
    if_show = models.BooleanField(default=True, verbose_name='是否显示')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '头条'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'分节标题', default='')
    detail = UEditorField(verbose_name=u"详情", width=600, height=300, imagePath="project/ueditor/",
                          filePath="club/ueditor/", default='')
    if_show = models.BooleanField(default=True, verbose_name='是否显示')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'成员名', default='')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,  default='', verbose_name=u'申请人')
    field = models.CharField(max_length=100, verbose_name=u'行业领域', default='')

    logo = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100,blank=True,
                             verbose_name=u'logo')
    status = models.CharField(max_length=20, default='1',
                              choices=(('-1', u'驳回'), ('0', u'审核中'), ('1', u'通过审核')),
                              verbose_name=u'审核状态')
    note = models.CharField(max_length=20, default='1', null=True, blank=True, verbose_name=u'审核意见')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '成员管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"资源名")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="club/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
