# _*_ coding: utf-8 _*_

from django.conf.urls import url
from .views import PatentListView, PatentDetailView, AddPatentView, ModifyView, SearchView

# from django.urls import path, re_path

app_name = "patent"

urlpatterns = [
    # 专利展示
    url(r'^list/$', PatentListView.as_view(), name='list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^detail/(?P<patent_id>\d+)/', PatentDetailView.as_view(), name='detail'),
    url(r'^add_patent/$', AddPatentView.as_view(), name='add_patent'),
    url(r'^modify/(?P<patent_id>\d+)/', ModifyView.as_view(), name='modify'),
]
