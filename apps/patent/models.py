# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile

from DjangoUeditor.models import UEditorField


# Create your models here.


class Patent(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'专利名', default='')
    seller = models.ForeignKey(UserProfile,on_delete=models.CASCADE,  default='', verbose_name=u'卖家')
    patent_id = models.CharField(max_length=100, verbose_name=u'专利申请号', default='')
    field_category = models.CharField(max_length=100, choices=(
        ('0', u'食品饮料'), ('1', u'建筑建材'), ('2', u'家居用品'), ('3', u'轻工纺织'), ('4', u'化学化工'), ('5', u'新能源'), ('6', u'机械'),
        ('7', u'环保和资源'), ('8', u'橡胶塑料'), ('9', u'仪器仪表'), ('10', u'新型材料'), ('11', u'电子信息'), ('12', u'医药与医疗'),
        ('13', u'农林牧业'), ('14', u'海洋开发'), ('15', u'航空航天'), ('16', u'采矿冶金'), ('17', u'电气自动化'), ('18', u'包装印刷'),
        ('19', u'教育休闲'), ('20', u'钒钛产业'), ('21', u'安全防护'), ('22', u'交通运输')), default='0', verbose_name=u'所属行业')
    patent_category = models.CharField(max_length=100, default='fmzl',
                                       choices=(('fmzl', u'发明专利'), ('syxxzl', u'实用新型专利'), ('wgzl', '外观专利')),
                                       verbose_name=u'专利类别')
    province = models.CharField(max_length=20, choices=(('bj', u'北京'), ('tj', u'天津')), default='bj',
                                verbose_name=u'专利所在地区')
    patent_expired = models.DateField(default=datetime.now, verbose_name=u'有效日期')
    main_pic = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100,
                                 verbose_name=u'专利主图')
    more_pic = models.ImageField(upload_to='image/%Y/%m', null=True, blank=True, max_length=100, verbose_name=u'专利图')
    price = models.IntegerField(default=0, verbose_name='价格')
    bargain = models.BooleanField(default=False, verbose_name='议价')
    hire = models.IntegerField(default=0, verbose_name='佣金')
    keyword = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'关键词')
    status = models.CharField(max_length=20, null=True, blank=True,
                              choices=(('sqwjf', u'授权未结费'), ('yxzs', u'已下证书')),
                              verbose_name=u'专利状态')
    IPC_num = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'分类号')
    application_date = models.DateField(null=True, blank=True, verbose_name=u'申请日期')
    agent = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'代理人')
    agency = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'代理机构')
    inventor = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'发明人')
    applicant = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'申请人')
    contact = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'联系人')
    contact_mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'联系电话')
    # 修改imagepath,不能传y m 进来，不能加斜杠是一个相对路径，相对于setting中配置的mediaroot
    detail = UEditorField(verbose_name=u"详情", width=600, height=300, imagePath="patent/ueditor/",
                          filePath="patent/ueditor/", default='')
    shop_status = models.CharField(max_length=20, default='1',
                                   choices=(('-1', u'已下架'), ('0', u'审核中'), ('1', u'已上架'), ('2', u'交易中'), ('3', u'已交易')),
                                   verbose_name=u'上架状态')
    if_show = models.BooleanField(default=False, verbose_name='是否显示')
    note = models.CharField(max_length=20, default='1', null=True, blank=True, verbose_name=u'审核意见')
    click_num = models.IntegerField(default=0, verbose_name=u'点击次数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏次数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')

    def get_seller_mobile(self):
        return self.seller.mobile

    get_seller_mobile.short_description = "卖家手机号"

    class Meta:
        verbose_name = '专利商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.shop_status == '1':
            self.if_show = True
        else:
            self.if_show = False
        super(self.__class__, self).save(*args, **kwargs)
