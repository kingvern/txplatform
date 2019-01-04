# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from patent.models import Patent
from project.models import Project


# Create your models here.

class UserAsk(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户', null=True)
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'其他慢慢加')), default=1,
                                   verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(
        choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'孵化器'), (4, u'科技园区'), (5, u'金融机构'), (6, u'展会'), (7, u'展会点赞')),
        default=1,
        verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserJoin(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    join_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    join_type = models.IntegerField(choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'展会')), default=1,
                                    verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户报名'
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
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'买家',
                              related_name='patent_buyer_set')
    order_name = models.CharField(max_length=100, default='', verbose_name=u'单位名称')
    order_address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    order_contact = models.CharField(max_length=100, default='', verbose_name=u'联系人')
    order_mobile = models.CharField(max_length=11, default='', verbose_name=u'手机')
    patent = models.ForeignKey(Patent, on_delete=models.CASCADE, verbose_name=u'专利')
    base_price = models.IntegerField(default=0, verbose_name=u'基础费')
    serve_fee = models.IntegerField(default=0, verbose_name=u'服务费')
    total_price = models.IntegerField(default=0, verbose_name=u'总费')
    step = models.CharField(max_length=10, default='0',
                            choices=(('-1', u'已取消'), ('0', u'下单未付款'), ('1', u'买家已付款'), ('2', u'已提交专利局'), ('3', u'交易完成')),
                            verbose_name=u'订单阶段')
    contract = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"合同",
        default='',
        null=True,
        blank=True,
        max_length=100)
    prof = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"付款凭证",
        default='', null=True,
        blank=True,
        max_length=100)
    step_time = models.DateTimeField(default=datetime.now, verbose_name=u'阶段时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name=u'业务员',
                              related_name='patent_staff_set')

    def get_seller_username(self):
        return self.patent.seller.username

    get_seller_username.short_description = "卖家名字"

    def get_seller_mobile(self):
        return self.patent.seller.mobile

    get_seller_mobile.short_description = "卖家手机号"

    class Meta:
        verbose_name = '专利交易管理'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.step_time = datetime.now()
        super(self.__class__, self).save(*args, **kwargs)


class BuyerProject(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'买家',
                              related_name='project_buyer_set')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'项目')
    step = models.CharField(max_length=10, default='0', choices=(
        ('0', u'等待支付定金'), ('1', u'平台合同签订'), ('2', u'三方协议签订'), ('3', u'履约完成'), ('-1', u'取消或终止')),
                            verbose_name=u'订单阶段')
    step_time = models.DateTimeField(default=datetime.now, verbose_name=u'阶段时间')
    contract = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"合同",
        default='', null=True,
        blank=True,
        max_length=100)
    prof = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"定金凭证",
        default='', null=True,
        blank=True,
        max_length=100)
    protocol = models.FileField(
        upload_to="protocol/resource/%Y/%m",
        verbose_name=u"协议",
        default='', null=True,
        blank=True,
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, verbose_name=u'业务员',
                              related_name='project_staff_set')

    def get_seller_username(self):
        return self.project.seller.username

    get_seller_username.short_description = "卖家名字"

    def get_seller_mobile(self):
        return self.project.seller.mobile

    get_seller_mobile.short_description = "卖家手机号"

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.step_time = datetime.now()
    # 有毒

    class Meta:
        verbose_name = '技术项目订单管理'
        verbose_name_plural = verbose_name
