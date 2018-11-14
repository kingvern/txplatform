# _*_ coding: utf-8 _*_

import xadmin

from .models import Organization, Expert, Couveuse, Park, Financial


class OrganizationAdmin(object):
    list_display = ['name', 'descs', 'click_num', 'fav_num', 'address', 'add_time']
    search_fields = ['name', 'descs', 'click_num', 'fav_num', 'address']
    list_filter = ['name', 'descs', 'click_num', 'fav_num', 'address', 'add_time']


class ExpertAdmin(object):
    list_display = ['Organization', 'name', 'descs', 'click_num', 'fav_num', 'filed', 'add_time']
    search_fields = ['Organization', 'name', 'descs', 'click_num', 'fav_num', 'filed']
    list_filter = ['Organization', 'name', 'descs', 'click_num', 'fav_num', 'filed', 'add_time']


class CouveuseAdmin(object):
    list_display = ['name', 'area0', 'area1', 'level', 'addr', 'if_recommend']
    search_fields = ['name', 'area0', 'area1', 'level', 'addr', 'if_recommend']
    list_filter = ['name', 'area0', 'area1', 'level', 'addr', 'if_recommend']


class ParkAdmin(object):
    list_display = ['name', 'area0', 'area1', 'addr', 'if_recommend']
    search_fields = ['name', 'area0', 'area1', 'addr', 'if_recommend']
    list_filter = ['name', 'area0', 'area1', 'addr', 'if_recommend']


class FinancialAdmin(object):
    list_display = ['name', 'area0', 'area1', 'type', 'addr', 'if_recommend']
    search_fields = ['name', 'area0', 'area1', 'type', 'addr', 'if_recommend']
    list_filter = ['name', 'area0', 'area1', 'type', 'addr', 'if_recommend']


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Expert, ExpertAdmin)
xadmin.site.register(Couveuse, CouveuseAdmin)
xadmin.site.register(Park, ParkAdmin)
xadmin.site.register(Financial, FinancialAdmin)
