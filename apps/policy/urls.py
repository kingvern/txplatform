# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import PolicyView, AddUserAskView


urlpatterns = [
    # 政策展示
    url(r'^list/$', PolicyView.as_view(), name='policy_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]
