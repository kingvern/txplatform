# _*_ encoding:utf-8 _*_

import xadmin
from xadmin import views
from .models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    # pass


class GlobalSetting(object):
    site_title = '技术交易平台管理系统'
    site_footer = ''
    menu_style = 'accordion'


class UserProfileAdmin(object):
    list_display = ['id', 'username', 'full_name', 'mobile', 'is_staff', 'last_login']
    search_fields = ['id', 'username', 'is_staff', 'full_name', 'last_login', 'mobile']
    list_filter = ['id', 'username', 'is_staff', 'full_name', 'last_login', 'mobile']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
