# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    full_name = models.CharField(max_length=50, verbose_name=u'姓名（实名）', default='')
    id_card = models.CharField(max_length=50, verbose_name=u'身份证号（实名）', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'性别')
    address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, default='', verbose_name=u'手机')
    avatar = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, null=True,
                               blank=True, verbose_name=u'头像')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    mobile = models.CharField(max_length=50, verbose_name=u'手机号')
    send_type = models.CharField(choices=(('register', u'注册'), ('reset_pwd', u'忘记密码'), ('update_mobile', u'更新手机号')),
                                 max_length=20)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'手机验证码'
        verbose_name_plural = verbose_name


class UpdateMobileRecord(models.Model):
    old_mobile = models.CharField(max_length=50, verbose_name=u'手机号')
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    new_mobile = models.CharField(max_length=50, verbose_name=u'手机号')
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'手机更新记录'
        verbose_name_plural = verbose_name
