# _*_ coding: utf-8 _*_

import xadmin

from .models import Patent, Category


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class PatentAdmin(object):
    list_display = ['name', 'seller', 'patent_id', 'field_category', 'patent_category', 'province', 'patent_expired',
                    'main_pic',
                    'more_pic', 'price', 'bargain', 'hire', 'keyword', 'IPC_num', 'application_date', 'agent', 'agency',
                    'inventor', 'applicant', 'contact', 'contact_mobile', 'detail', 'click_num', 'fav_num', 'add_time']
    search_fields = ['name', 'seller', 'patent_id', 'field_category', 'patent_category', 'province', 'patent_expired',
                     'main_pic',
                     'more_pic', 'price', 'bargain', 'hire', 'keyword', 'IPC_num', 'agent', 'agency',
                     'inventor', 'applicant', 'contact', 'contact_mobile', 'detail', 'click_num', 'fav_num']
    list_filter = ['name', 'seller', 'patent_id', 'field_category', 'patent_category', 'province', 'patent_expired',
                   'main_pic',
                   'more_pic', 'price', 'bargain', 'hire', 'keyword', 'IPC_num', 'application_date', 'agent', 'agency',
                   'inventor', 'applicant', 'contact', 'contact_mobile', 'detail', 'click_num', 'fav_num', 'add_time']

    # 富文本
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Patent, PatentAdmin)
