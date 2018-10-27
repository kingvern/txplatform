# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, MyFavView, MyMessageView, MyOrderView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # 政策展示

    url('info/', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    url('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 用户中心我的课程
    url('myorder/', MyOrderView.as_view(), name="myorder"),

    # 我收藏的课程机构
    url('myfav/', MyFavView.as_view(), name="myfav"),

    url('my_message/', MyMessageView.as_view(), name="my_message"),
]
