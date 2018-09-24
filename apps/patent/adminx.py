# _*_ coding: utf-8 _*_

import xadmin

from .models import Patent, Category


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class PatentAdmin(object):
    list_display = ['Category', 'name', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']
    search_fields = ['Category', 'name', 'detail', 'click_num', 'fav_num']
    list_filter = ['Category', 'name', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Patent, PatentAdmin)
