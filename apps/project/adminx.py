# _*_ coding: utf-8 _*_

import xadmin

from .models import Project, Projectt


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
#
#
# class ProjecttAdmin(object):
#     list_display = ['id', 'name', 'shop_status']
#     search_fields = ['id', 'name', 'shop_status']
#     list_filter = ['id', 'name', 'shop_status']
#     list_editable = ['note', 'shop_status']
#     # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
#     relfield_style = 'fk-ajax'
#     # 后台默认排序
#     ordering = ['shop_status']
#     # 后台可选刷新频率
#     refresh_times = [3, 5]
#     style_fields = {"detail": "ueditor"}


xadmin.site.register(Project, ProjectAdmin)
# xadmin.site.register(Projectt, ProjecttAdmin)
