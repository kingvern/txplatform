# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile

from DjangoUeditor.models import UEditorField


# Create your models here.


class SSDPatent(models.Model):
    pid = models.CharField(max_length=50, verbose_name=u'专利编码', default='', null=True, blank=True)
    tic = models.CharField(max_length=50, verbose_name=u'标题-中文', default='', null=True, blank=True)
    tie = models.CharField(max_length=500, verbose_name=u'标题-英文', default='', null=True, blank=True)
    tio = models.CharField(max_length=50, verbose_name=u'标题-原始', default='', null=True, blank=True)
    ano = models.CharField(max_length=50, verbose_name=u'申请号-原始', default='', null=True, blank=True)
    ad = models.CharField(max_length=50, verbose_name=u'申请日', default='', null=True, blank=True)
    pd = models.CharField(max_length=50, verbose_name=u'公开日', default='', null=True, blank=True)
    pK = models.CharField(max_length=50, db_column='pk', verbose_name=u'文献类型', default='', null=True, blank=True)
    pno = models.CharField(max_length=50, verbose_name=u'文献号-原始', default='', null=True, blank=True)
    apo = models.CharField(max_length=50, verbose_name=u'申请人-原始', default='', null=True, blank=True)
    ape = models.CharField(max_length=200, verbose_name=u'申请人-英文', default='', null=True, blank=True)
    apc = models.CharField(max_length=50, verbose_name=u'申请人-中文', default='', null=True, blank=True)
    ipc = models.CharField(max_length=200, verbose_name=u'IPC', default='', null=True, blank=True)
    lc = models.CharField(max_length=50, verbose_name=u'洛迦诺分类', default='', null=True, blank=True)
    vu = models.CharField(max_length=50, verbose_name=u'专利强度', default='', null=True, blank=True)
    abso = models.TextField(max_length=1000, verbose_name=u'摘要-原始语种', default='', null=True, blank=True)
    abse = models.TextField(max_length=2000, verbose_name=u'摘要-英文', default='', null=True, blank=True)
    absc = models.TextField(max_length=1000, verbose_name=u'摘要-中文', default='', null=True, blank=True)
    imgtitle = models.CharField(max_length=50, verbose_name=u'缩略图', default='', null=True, blank=True)
    imgname = models.CharField(max_length=200, verbose_name=u'缩略图名称', default='', null=True, blank=True)
    # IMGTITLE = models.CharField(max_length=50, verbose_name=u'缩略图', default='', null=True, blank=True)
    # IMGNAME = models.CharField(max_length=50, verbose_name=u'缩略图名称', default='', null=True, blank=True)
    lssc = models.CharField(max_length=50, verbose_name=u'当前权利状态', default='', null=True, blank=True)
    pdt = models.CharField(max_length=50, verbose_name=u'专利类型', default='', null=True, blank=True)
    debec = models.TextField(max_length=1000, verbose_name=u'简要说明-中文', default='', null=True, blank=True)
    debeo = models.TextField(max_length=1000, verbose_name=u'简要说明-原始', default='', null=True, blank=True)
    debee = models.TextField(max_length=1000, verbose_name=u'简要说明-英文', default='', null=True, blank=True)
    depc = models.TextField(max_length=1000, verbose_name=u'简要说明-英文', default='', null=True, blank=True)
    imgo = models.CharField(max_length=200, verbose_name=u'原始图', default='', null=True, blank=True)
    # IMGO = models.CharField(max_length=50, verbose_name=u'原始图', default='', null=True, blank=True)
    absoimgpath = models.CharField(max_length=200, verbose_name=u'摘要图', default='', null=True, blank=True)
    pdfexist = models.CharField(max_length=50, verbose_name=u'是否存在PDF', default='', null=True, blank=True)
    ans = models.CharField(max_length=50, verbose_name=u'申请号标准', default='', null=True, blank=True)
    pns = models.CharField(max_length=50, verbose_name=u'公布号标准', default='', null=True, blank=True)
    sfpns = models.CharField(max_length=50, verbose_name=u'代表性文献号', default='', null=True, blank=True)
    inc = models.CharField(max_length=200, verbose_name=u'发明人-中文', default='', null=True, blank=True)
    ine = models.CharField(max_length=200, verbose_name=u'发明人-英文', default='', null=True, blank=True)
    ino = models.CharField(max_length=200, verbose_name=u'发明人-原文', default='', null=True, blank=True)
    agc = models.CharField(max_length=50, verbose_name=u'代理人-中文', default='', null=True, blank=True)
    age = models.CharField(max_length=200, verbose_name=u'代理人-英文', default='', null=True, blank=True)
    ago = models.CharField(max_length=50, verbose_name=u'代理人-原文', default='', null=True, blank=True)
    asc = models.CharField(max_length=50, verbose_name=u'专利权人-中文', default='', null=True, blank=True)
    ase = models.CharField(max_length=200, verbose_name=u'专利权人-英文', default='', null=True, blank=True)
    aso = models.CharField(max_length=50, verbose_name=u'专利权人-原文', default='', null=True, blank=True)
    exc = models.CharField(max_length=50, verbose_name=u'审查员-中文', default='', null=True, blank=True)
    exe = models.CharField(max_length=200, verbose_name=u'审查员人-英文', default='', null=True, blank=True)
    exo = models.CharField(max_length=50, verbose_name=u'审查员-原文', default='', null=True, blank=True)
    pdf = models.CharField(max_length=200, verbose_name=u'pdf地址', default='', null=True, blank=True)

    cro = models.CharField(max_length=300, verbose_name=u'cro', default='', null=True, blank=True)
    cre = models.CharField(max_length=800, verbose_name=u'cre', default='', null=True, blank=True)
    crc = models.CharField(max_length=300, verbose_name=u'crc', default='', null=True, blank=True)
    cri = models.CharField(max_length=300, verbose_name=u'cri', default='', null=True, blank=True)

    addd = models.DateTimeField(default=None, null=True, blank=True, verbose_name=u'addd日期')
    pdd = models.DateTimeField(default=None, null=True, blank=True, verbose_name=u'pdd日期')

    imgnamee = models.ImageField(default=None, upload_to='image/%Y/%m', null=True, blank=True, max_length=100,
                                 verbose_name=u'imgnamee')
    imgoo = models.ImageField(default=None, upload_to='image/%Y/%m', null=True, blank=True, max_length=100,
                              verbose_name=u'imgoo')
    absoimgpathh = models.ImageField(default=None, upload_to='image/%Y/%m', null=True, blank=True, max_length=100,
                                     verbose_name=u'absoimgpathh')
    pdff = models.FileField(default=None, upload_to='pdf/%Y/%m', null=True, blank=True, max_length=100,
                            verbose_name=u'pdff')

    price = models.IntegerField(default=0, verbose_name='价格')
    bargain = models.BooleanField(default=True, verbose_name='议价')

    if_success = models.BooleanField(default=False, verbose_name='是否为成功案例')

    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, verbose_name=u'卖家', null=True,
                               blank=True)
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
        return self.tio

    def save(self, *args, **kwargs):
        # ('-1', u'已下架'), ('0', u'审核中'), ('1', u'已上架'), ('2', u'交易中'), ('3', u'已交易')
        if self.shop_status == '1':
            self.if_show = True
        else:
            self.if_show = False
        super(self.__class__, self).save(*args, **kwargs)
