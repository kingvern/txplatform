# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import PatentListView,PatentDetailView
# from django.urls import path, re_path

app_name = "patent"


urlpatterns = [
    # 专利展示
    url(r'^list/$', PatentListView.as_view(), name='list'),
    url(r'^detail/(?P<patent_id>\d+)/', PatentDetailView.as_view(), name='detail')

    # re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
]
