# _*_ coding: utf-8 _*_


import xadmin

from .models import UserAsk, UserFavorite, UserMessage, UserPatent


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


class UserPatentAdmin(object):
    list_display = ['user', 'patent', 'add_time']
    search_fields = ['user', 'patent']
    list_filter = ['user', 'patent', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserPatent, UserPatentAdmin)
