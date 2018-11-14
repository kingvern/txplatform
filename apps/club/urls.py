# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import HomeView

# from django.urls import path, re_path

app_name = "club"

urlpatterns = [
    url('home/', HomeView.as_view(), name="home"),

]
