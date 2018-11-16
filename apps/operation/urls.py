# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import AddFavView, AddJoinView, CancelPublishView, \
    DeletePublishView, OrderView, CancelOrderView, DeleteOrderView

# from django.urls import path, re_path

app_name = "operation"

urlpatterns = [
    url('add_fav/', AddFavView.as_view(), name="add_fav"),
    url('add_join/', AddJoinView.as_view(), name="add_join"),

    url('add_order/', OrderView.as_view(), name="order"),

    url('modify_publish/', CancelPublishView.as_view(), name="modify_publish"),
    url('cancel_publish/', CancelPublishView.as_view(), name="cancel_publish"),
    url('delete_publish/', DeletePublishView.as_view(), name="delete_publish"),

    url('cancel_order/', CancelOrderView.as_view(), name="cancel_order"),
    url('delete_order/', DeleteOrderView.as_view(), name="delete_order"),
]
