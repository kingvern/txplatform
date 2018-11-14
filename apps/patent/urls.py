# _*_ coding: utf-8 _*_

from django.conf.urls import url
from .views import PatentListView, PatentDetailView, AddPatentView

# from django.urls import path, re_path

app_name = "patent"

urlpatterns = [
    # 专利展示
    url(r'^list/$', PatentListView.as_view(), name='list'),
    url(r'^detail/(?P<patent_id>\d+)/', PatentDetailView.as_view(), name='detail'),
    url(r'^add_patent/$', AddPatentView.as_view(), name='add_patent'),

]
