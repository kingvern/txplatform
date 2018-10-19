# _*_ coding: utf-8 _*_


import xadmin

from .models import UserAsk, UserFavorite, UserMessage, BuyerPatent, BuyerProject


class UserAskAdmin(object):
    list_display = ['name', 'policy_name', 'add_time']
    search_fields = ['name', 'policy_name']
    list_filter = ['name', 'policy_name', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class BuyerPatentAdmin(object):
    list_display = ['seller', 'patent', 'add_time']
    search_fields = ['seller', 'patent']
    list_filter = ['seller', 'patent', 'add_time']

class BuyerProjectAdmin(object):
    list_display = ['seller', 'project', 'add_time']
    search_fields = ['seller', 'project']
    list_filter = ['seller', 'project', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(BuyerPatent, BuyerPatentAdmin)
xadmin.site.register(BuyerProject, BuyerProjectAdmin)
