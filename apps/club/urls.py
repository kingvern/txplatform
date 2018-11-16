# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import HomeView, DetailView,AddMemberView

# from django.urls import path, re_path

app_name = "club"

urlpatterns = [
    url('home/', HomeView.as_view(), name="home"),

    url('section/(?P<section_id>\d+)/', DetailView.as_view(), name='section'),

    url('add_member/$', AddMemberView.as_view(), name='add_member'),

]
