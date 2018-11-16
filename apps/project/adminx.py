# _*_ coding: utf-8 _*_

import xadmin

from .models import Project

class ProjectAdmin(object):
    list_display = ['id', 'name', 'get_seller_mobile', 'project_step', 'cooperation', 'province', 'price', 'click_num',
                    'fav_num', 'shop_status', 'note']
    search_fields = ['id', 'name', 'seller', 'project_step', 'cooperation', 'province', 'price', 'click_num', 'fav_num',
                     'shop_status', 'note']
    list_filter = ['id', 'name', 'seller', 'project_step', 'cooperation', 'province', 'price', 'click_num', 'fav_num',
                   'shop_status', 'note']
    list_editable = ['note', 'shop_status']
    # # 后台默认排序
    ordering = ['shop_status']
    # # 后台可选刷新频率
    refresh_times = [3, 5]
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Project, ProjectAdmin)
