# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    full_name = models.CharField(max_length=50, verbose_name=u'姓名（实名）', default='')
    id_num = models.CharField(max_length=50, verbose_name=u'身份证号（实名）', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name=u'性别')
    address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机')
    avatar = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, null=True, blank=True, verbose_name=u'头像')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('reset_pwd', u'忘记密码')), max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class MobileVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    mobile = models.EmailField(max_length=50, verbose_name=u'手机号')
    send_type = models.CharField(choices=(('register', u'注册'), ('reset_pwd', u'忘记密码')), max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'手机验证码'
        verbose_name_plural = verbose_name