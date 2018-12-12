# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, MyFavView, MyMessageView, MyOrderView, \
    ForCodeView, MyPublishView, UserAuthView, MyFavPolicyView, \
    MyFavIncubatorView, MyFavGalleryView

urlpatterns = [
    # 中心展示
    url('info/', UserInfoView.as_view(), name="user_info"),
    url('auth/', UserAuthView.as_view(), name="user_auth"),
    url('safe/', UserAuthView.as_view(), name="user_safe"),

    # 用户头像上传
    url('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 用户中心我的课程
    url('myorder/', MyOrderView.as_view(), name="myorder"),

    url('myfav/', MyFavView.as_view(), name="myfav"),

    url('myPublish/', MyPublishView.as_view(), name="mypublish"),

    url('my_message/', MyMessageView.as_view(), name="my_message"),

    url('forcode/', ForCodeView.as_view(), name='forcode'),

    url('fav_policy/', MyFavPolicyView.as_view(), name="fav_policy"),
    url('fav_incubator/', MyFavIncubatorView.as_view(), name="fav_incubator"),
    url('fav_gallery/', MyFavGalleryView.as_view(), name="fav_gallery"),
]
