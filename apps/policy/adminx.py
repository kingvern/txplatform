# _*_ coding: utf-8 _*_

import xadmin

from .models import Province, Department, Policy, Banner, Chart

# 显示更新时间
class ProvinceAdmin(object):
    list_display = ['name', 'if_show']
    search_fields = ['name', 'if_show']
    list_filter = ['name', 'if_show']


class DepartmentAdmin(object):
    list_display = ['name', 'if_show']
    search_fields = ['name', 'if_show']
    list_filter = ['name', 'if_show']


class PolicyAdmin(object):
    list_display = ['policy_id', 'title', 'addr', 'source', 'click_num', 'fav_num', 'pubDate']
    search_fields = ['policy_id', 'title', 'addr', 'source', 'click_num', 'fav_num', 'pubDate']
    list_filter = ['policy_id', 'title', 'addr', 'source', 'click_num', 'fav_num', 'pubDate']


class BannerAdmin(object):
    list_display = ['title', 'detail', 'click_num', 'fav_num', 'if_show', 'add_time']
    search_fields = ['title', 'detail', 'click_num', 'fav_num', 'if_show']
    list_filter = ['title', 'detail', 'click_num', 'fav_num', 'if_show', 'add_time']


class ChartAdmin(object):
    list_display = ['tab', 'tab2', 'title', 'type', 'data', 'click_num', 'fav_num', 'add_time']
    search_fields = ['tab', 'tab2', 'title', 'type', 'data', 'click_num', 'fav_num']
    list_filter = ['tab', 'tab2', 'title', 'type', 'data', 'click_num', 'fav_num', 'add_time']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Policy, PolicyAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Chart, ChartAdmin)
