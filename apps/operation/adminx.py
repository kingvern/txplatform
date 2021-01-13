# _*_ coding: utf-8 _*_


import xadmin

from .models import UserAsk, UserFavorite, UserMessage, BuyerPatent, BuyerProject, PatentComments, MessageBoard

from datetime import datetime


class UserAskAdmin(object):
    list_display = ['user', 'add_time']
    search_fields = ['user', ]
    list_filter = ['user', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


# 卖家 业务员 合同 资料(业务员上传) 业务员接收
class BuyerPatentAdmin(object):
    list_display = ['id', 'patent', 'get_seller_username', 'get_seller_mobile', 'buyer', 'total_price', 'contract',
                    'prof', 'step', 'step_time', 'add_time', 'staff']
    search_fields = ['id', 'patent__tic', 'buyer__username', 'buyer__mobile', 'total_price', 'step']
    list_filter = ['id', 'patent', 'buyer', 'total_price', 'step']
    refresh_times = [3, 5]
    list_editable = ['contract', 'prof', 'step', 'staff']

    # SSDPatent shop_status ('-1', u'已下架'), ('0', u'审核中'), ('1', u'已上架'), ('2', u'交易中'), ('3', u'已交易')
    # BuyerPatent step ('-1', u'已取消'), ('0', u'下单未付款'), ('1', u'买家已付款'), ('2', u'已提交专利局'), ('3', u'交易完成')
    # bingo
    def save_models(self):
        obj = self.new_obj
        obj.step_time = datetime.now()
        obj.save()
        if obj.step == '-1':
            patent = obj.patent
            patent.shop_status = 1
            patent.save()
        if obj.step in ['0', '1', '2']:
            patent = obj.patent
            patent.shop_status = 2
            patent.save()
        if obj.step == '3':
            patent = obj.patent
            patent.shop_status = 3
            patent.save()


# 卖家 业务员 合同 资料(业务员上传) 业务员接收
class BuyerProjectAdmin(object):
    list_display = ['id', 'project', 'get_seller_username', 'get_seller_mobile', 'buyer', 'step', 'contract', 'prof',
                    'protocol', 'staff']
    search_fields = ['id', 'project__name', 'buyer__username', 'buyer__mobile', 'step', 'contract', 'prof',
                     'protocol']
    list_filter = ['id', 'project', 'buyer', 'step', 'contract', 'prof',
                   'protocol']
    refresh_times = [3, 5]
    relfield_style = 'fk-ajax'
    list_editable = ['step', 'contract', 'prof', 'protocol', 'staff']


class PatentCommentsAdmin(object):
    list_display = ['id', 'patent', 'contact_name', 'contact_phone', 'budget', 'add_time']
    search_fields = ['id', 'patent', 'contact_name', 'contact_phone', 'budget', 'add_time']
    list_filter = ['id', 'patent', 'contact_name', 'contact_phone', 'budget', 'add_time']


class MessageBoardAdmin(object):
    list_display = ['id', 'patent_name', 'category', 'contact_name', 'contact_phone', 'budget', 'add_time',  'if_show']
    search_fields = ['id', 'patent_name', 'category', 'contact_name', 'contact_phone', 'budget', 'add_time', 'comments', 'if_show']
    list_filter = ['id', 'patent_name', 'category', 'contact_name', 'contact_phone', 'budget', 'add_time',  'if_show']
    relfield_style = 'fk-ajax'
    list_editable = ['if_show']


# xadmin.site.register(UserAsk, UserAskAdmin)
# xadmin.site.register(UserFavorite, UserFavoriteAdmin)
# xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(BuyerPatent, BuyerPatentAdmin)
# xadmin.site.register(PatentComments, PatentCommentsAdmin)
xadmin.site.register(MessageBoard, MessageBoardAdmin)
