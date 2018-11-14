# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import AddFavView, AddJoinView

# from django.urls import path, re_path

app_name = "operation"

urlpatterns = [
    url('add_fav/', AddFavView.as_view(), name="add_fav"),
    url('add_join/', AddJoinView.as_view(), name="add_join"),
]
