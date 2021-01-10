# _*_ coding: utf-8 _*_

from django.conf.urls import url
from .views import SSDPatentListView, SSDPatentDetailView, AddSSDPatentView, ModifyView, SearchView, SavePatentView

# from django.urls import path, re_path

app_name = "ssdpatent"

urlpatterns = [
    # 专利展示
    url(r'^list/$', SSDPatentListView.as_view(), name='list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^detail/(?P<patent_id>\d+)/', SSDPatentDetailView.as_view(), name='detail'),
    url(r'^add_patent/', AddSSDPatentView.as_view(), name='add_patent'),
    url(r'^modify/(?P<patent_id>\d+)/', ModifyView.as_view(), name='modify'),
    url(r'^save_patent/', SavePatentView.as_view(), name='save_patent'),
]
