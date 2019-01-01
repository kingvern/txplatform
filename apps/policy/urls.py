# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from .views import PolicyListView, PolicyDetailView, AddChartView, \
    AddPolicyView, chartDataView, PolicyBannerView, PolicyHomeView, SearchView, RecordTimeView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # 政策展示

    url(r'^recordTime/$', csrf_exempt(RecordTimeView.as_view()), name='recordTime'),
    url(r'^home/$', PolicyHomeView.as_view(), name='home'),
    url(r'^list/$', PolicyListView.as_view(), name='list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^chartData/$', csrf_exempt(chartDataView.as_view()), name='chartData'),
    url(r'^addPolicy/$', csrf_exempt(AddPolicyView.as_view()), name='addPolicy'),
    url(r'^addChart/$', csrf_exempt(AddChartView.as_view()), name='addChart'),
    url(r'^detail/(?P<policy_id>\d+)/', PolicyDetailView.as_view(), name='detail'),
    url(r'^banner/(?P<banner_id>\d+)/', PolicyBannerView.as_view(), name='banner'),
]
