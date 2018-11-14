# _*_ coding: utf-8 _*_

import xadmin

from .models import Gallery


class GalleryAdmin(object):
    list_display = ['name', 'pic', 'descs', 'addr', 'time_begin', 'time_end', 'status', 'if_recommend']
    search_fields = ['name', 'pic', 'descs', 'addr', 'status', 'if_recommend']
    list_filter = ['name', 'pic', 'descs', 'addr', 'time_begin', 'time_end', 'status', 'if_recommend']


xadmin.site.register(Gallery, GalleryAdmin)
