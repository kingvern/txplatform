# _*_ coding: utf-8 _*_

import xadmin

from .models import Project, Category


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class ProjectAdmin(object):
    list_display = ['name', 'field_category', 'project_step', 'cooperation', 'province', 'price', 'bargain', 'hire',
                    'keyword', 'status', 'detail', 'click_num', 'fav_num', 'add_time']
    search_fields = ['name', 'field_category', 'project_step', 'cooperation', 'province', 'price', 'bargain', 'hire',
                     'keyword', 'status', 'detail', 'click_num', 'fav_num']
    list_filter = ['name', 'field_category', 'project_step', 'cooperation', 'province', 'price', 'bargain', 'hire',
                   'keyword', 'status', 'detail', 'click_num', 'fav_num', 'add_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Project, ProjectAdmin)
