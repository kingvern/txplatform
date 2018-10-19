# _*_ coding: utf-8 _*_

import xadmin

from .models import Province, Department, Policy


class ProvinceAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class DepartmentAdmin(object):
    list_display = ['name', 'Province']
    search_fields = ['name', 'Province']
    list_filter = ['name', 'Province']


class PolicyAdmin(object):
    list_display = ['name', 'Province', 'Department', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']
    search_fields = ['name', 'Province', 'Department', 'detail', 'click_num', 'fav_num']
    list_filter = ['name', 'Province', 'Department', 'detail', 'click_num', 'fav_num', 'publish_time', 'add_time']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Policy, PolicyAdmin)
