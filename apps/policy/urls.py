# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import PolicyListView, PolicyDetailView, AddChartView, \
    AddPolicyView, chartDataView, PolicyBannerView, PolicyHomeView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # 政策展示

    url(r'^home/$', PolicyHomeView.as_view(), name='home'),
    url(r'^list/$', PolicyListView.as_view(), name='list'),
    # url(r'^listAData/$', APolicyDataView.as_view(), name='listAData'),
    # url(r'^listBData/$', BPolicyDataView.as_view(), name='listBData'),
    url(r'^chartData/$', csrf_exempt(chartDataView.as_view()), name='chartData'),
    url(r'^addPolicy/$', csrf_exempt(AddPolicyView.as_view()), name='addPolicy'),
    url(r'^addChart/$', csrf_exempt(AddChartView.as_view()), name='addChart'),
    url(r'^detail/(?P<policy_id>\d+)/', PolicyDetailView.as_view(), name='detail'),
    url(r'^banner/(?P<banner_id>\d+)/', PolicyBannerView.as_view(), name='banner'),
]
