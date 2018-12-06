# _*_ coding: utf-8 _*_
"""platorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from platorm.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ResetPwdView, UpdateMobileView, LogoutView, IndexView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),

    url('^$', IndexView.as_view(), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^reset_pwd/$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'^update_mobile/$', UpdateMobileView.as_view(), name='update_mobile'),

    url(r'^users/', include('users.urls', namespace='users')),

    url(r'^policy/', include('policy.urls', namespace='policy')),
    url(r'^patent/', include('patent.urls', namespace='patent')),
    url(r'^project/', include('project.urls', namespace='project')),

    url(r'^incubator/', include('incubator.urls', namespace='incubator')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^club/', include('club.urls', namespace='club')),

    url("operation/", include('operation.urls', namespace="operation")),

    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 配置上传文件访问处理的函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
