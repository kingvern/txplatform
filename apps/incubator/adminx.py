# _*_ coding: utf-8 _*_

import xadmin

from .models import Organization, Expert


class OrganizationAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'address', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'address']
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'address', 'add_time']


class ExpertAdmin(object):
    list_display = ['Organization', 'name', 'desc', 'click_num', 'fav_num', 'filed', 'add_time']
    search_fields = ['Organization', 'name', 'desc', 'click_num', 'fav_num', 'filed']
    list_filter = ['Organization', 'name', 'desc', 'click_num', 'fav_num', 'filed', 'add_time']


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Expert, ExpertAdmin)
