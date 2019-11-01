# _*_ coding: utf-8 _*_
"""txplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  path(r'^blog/', include(blog_urls))
"""
import os

from django.urls import path, include, re_path
# from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from txplatform import settings

from txplatform.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ResetPwdView, UpdateMobileView, LogoutView, IndexView

urlpatterns = [
    path('admin/', xadmin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    path('reset_pwd/', ResetPwdView.as_view(), name='reset_pwd'),
    path('update_mobile/', UpdateMobileView.as_view(), name='update_mobile'),

    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('policy/', include(('policy.urls', 'policy'), namespace='policy')),
    path('patent/', include(('patent.urls', 'patent'), namespace='patent')),
    path('project/', include(('project.urls', 'project'), namespace='project')),

    path('incubator/', include(('incubator.urls', 'incubator'), namespace='incubator')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('club/', include(('club.urls', 'club'), namespace='club')),

    path("operation/", include(('operation.urls', 'operation'), namespace="operation")),

    path('ueditor/', include('DjangoUeditor.urls')),

    # 配置上传文件访问处理的函数
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)
