# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import ProjectListView, ProjectDetailView, AddProjectView, ModifyView, SearchView

# from django.urls import path, re_path

app_name = "project"

urlpatterns = [
    # 专利展示
    url(r'^list/$', ProjectListView.as_view(), name='list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^detail/(?P<project_id>\d+)/', ProjectDetailView.as_view(), name='detail'),
    url(r'^add_project/$', AddProjectView.as_view(), name='add_project'),
    url(r'^modify/(?P<project_id>\d+)/', ModifyView.as_view(), name='modify'),
]
