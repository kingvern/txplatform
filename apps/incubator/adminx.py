# _*_ coding: utf-8 _*_

import xadmin

from .models import Couveuse, Park, Financial



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


xadmin.site.register(Couveuse, CouveuseAdmin)
xadmin.site.register(Park, ParkAdmin)
xadmin.site.register(Financial, FinancialAdmin)
