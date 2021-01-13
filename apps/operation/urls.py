# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import AddFavView, AddJoinView, CancelPublishView, \
    DeletePublishView, OrderView, CancelOrderView, DeleteOrderView, GetOrderPDF, AddCommentsView, MessageBoardView, \
    DeleteMessageBoardView, MessageBoardListView, MessageBoardDetailView

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

    url('get_order_pdf/', GetOrderPDF.as_view(), name="get_order_pdf"),

    url('delete_message_board/', DeleteMessageBoardView.as_view(), name="delete_message_board"),

    url(r'message_board_list/', MessageBoardListView.as_view(), name="message_board_list"),

    url(r'^message_board_detail/(?P<messageboard_id>\d+)/', MessageBoardDetailView.as_view(), name='message_board_detail'),




    url(r'add_comment/', AddCommentsView.as_view(), name="add_comment")
]
