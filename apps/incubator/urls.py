# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import ListView, DetailView

# from django.urls import path, re_path

app_name = "incubator"

urlpatterns = [
    url(r'^list/$', ListView.as_view(), name='list'),
    url(r'^detail/(?P<incubator_id>\d+)/', DetailView.as_view(), name='detail'),

]
