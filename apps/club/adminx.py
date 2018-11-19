# _*_ coding: utf-8 _*_

import xadmin

from .models import Banner, Section, Member, Resource


class BannerAdmin(object):
    list_display = ['title', 'pic', 'if_show', 'click_num', 'fav_num']
    search_fields = ['title', 'pic', 'if_show', 'click_num', 'fav_num']
    list_filter = ['title', 'pic', 'if_show', 'click_num', 'fav_num']
    # 富文本
    style_fields = {"detail": "ueditor"}


class SectionAdmin(object):
    list_display = ['title', 'detail', 'if_show', 'click_num', 'fav_num']
    search_fields = ['title', 'detail', 'if_show', 'click_num', 'fav_num']
    list_filter = ['title', 'detail', 'if_show', 'click_num', 'fav_num']
    # 富文本
    style_fields = {"detail": "ueditor"}


class MemberAdmin(object):
    list_display = ['name', 'user', 'logo', 'status', 'note']
    search_fields = ['name', 'user', 'logo', 'status', 'note']
    list_filter = ['name', 'user', 'logo', 'status', 'note']
    list_editable = ['status', 'note']


class ResourceAdmin(object):
    list_display = ['name', 'download']
    search_fields = ['name', 'download']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Section, SectionAdmin)
xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(Resource, ResourceAdmin)
