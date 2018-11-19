# _*_ coding: utf-8 _*_

import xadmin

from .models import Patent


class PatentAdmin(object):
    list_display = ['id','name', 'seller', 'patent_id', 'patent_category',  'price', 'keyword', 'click_num', 'fav_num', 'shop_status', 'note']
    search_fields = ['id','name', 'seller', 'patent_id', 'patent_category',  'price',  'click_num', 'fav_num', 'shop_status', 'note']
    list_filter = ['id','name', 'seller', 'patent_id', 'patent_category',  'price',  'click_num', 'fav_num', 'shop_status', 'note']
    list_editable = ['note', 'shop_status']
    refresh_times = [3, 5]
    # 富文本
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Patent, PatentAdmin)
