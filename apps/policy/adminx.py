# _*_ coding: utf-8 _*_

import xadmin

from .models import Province, Department, Policy


class ProvinceAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class DepartmentAdmin(object):
    list_display = ['Province', 'name']
    search_fields = ['Province', 'name']
    list_filter = ['Province', 'name']


class PolicyAdmin(object):
    list_display = ['Province', 'Department', 'name', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']
    search_fields = ['Province', 'Department', 'name', 'detail', 'click_num', 'fav_num']
    list_filter = ['Province', 'Department', 'name', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Policy, PolicyAdmin)
