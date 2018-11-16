# _*_ coding: utf-8 _*_


import xadmin

from .models import UserAsk, UserFavorite, UserMessage, BuyerPatent, BuyerProject


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
    list_display = ['id', 'patent', 'get_seller_username', 'get_seller_mobile', 'buyer', 'total_price', 'step',
                    'step_time']
    search_fields = ['id', 'patent', 'total_price', 'step', 'step_time', 'buyer', ]
    list_filter = ['id', 'patent', 'total_price', 'step', 'step_time', 'buyer', ]
    refresh_times = [3, 5]
    list_editable = ['step', ]


# 卖家 业务员 合同 资料(业务员上传) 业务员接收
class BuyerProjectAdmin(object):
    list_display = ['id', 'project', 'step', 'step_time', 'contract', 'prof', 'protocol']
    search_fields = ['id', 'project', 'step', 'contract', 'prof', 'protocol']
    list_filter = ['id', 'project', 'step', 'step_time', 'contract', 'prof', 'protocol']
    refresh_times = [3, 5]
    list_editable = ['step', 'contract', 'prof', 'protocol']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(BuyerPatent, BuyerPatentAdmin)
xadmin.site.register(BuyerProject, BuyerProjectAdmin)
