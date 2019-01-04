# _*_ coding: utf-8 _*_
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse

from .models import Policy, Department, Province, Banner, Chart

from .forms import AddPolicyForm, AddChartForm
from operation.models import UserFavorite
import json


# Create your views here.

class PolicyHomeView(View):
    def get(self, request):
        banner_main = Banner.objects.filter(if_toutiao=True)[:1][0]
        banners = Banner.objects.filter(if_show=True)[1:4]

        policy = Policy.objects.filter(Q(source__if_show=True) & Q(addr__if_show=True)).order_by('-pubDate')[:20]

        return render(request, 'policy-home.html', {
            'banner_main': banner_main,
            'banners': banners,
            'policy_list': policy,
        })


class PolicyListView(View):
    def get(self, request):
        all_policy = Policy.objects.all().order_by('pubDate')
        provinces = Province.objects.all()
        all_department = Department.objects.all()

        policy = all_policy.filter(Q(source__if_show=True) & Q(addr__if_show=True))

        main = '0'
        mains = [u'中央', u'北京', u'天津', u'河北']
        province_id = request.GET.get('province', '3')
        if province_id:
            policy = policy.filter(addr=province_id)
            main = provinces.get(id=province_id).main

        provinceArray = []
        for main_ in range(4):
            province = provinces.filter(main=main_)
            provinceArray.append(province)

        policy = policy.order_by('source')
        departments_id = policy.values('source').distinct()
        departments = []
        for department_ in departments_id:
            departments.append(all_department.get(id=department_['source']))

        department_id = request.GET.get('department', '')
        if department_id:
            policy = policy.filter(source=department_id)

        policy = policy.order_by('-pubDate')
        policy_nums = policy.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(policy, 15, request=request)
        policy_data = p.page(page)

        for policy_ in policy_data.object_list:
            policy_.has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=policy_.id, fav_type=0):
                    policy_.has_fav = True

        return render(request, 'policy-list.html', {
            'main': main,
            'mains': mains,
            'policy_nums': policy_nums,
            'province_id': province_id,
            'provincesArray': provinceArray,
            'department_id': department_id,
            'departments': departments,
            'policy': policy_data,
        })


class SearchView(View):
    def get(self, request):
        policy = Policy.objects.all().filter(Q(source__if_show=True) & Q(addr__if_show=True))
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            policy = policy.filter(Q(title__icontains=search_keywords) | Q(info__icontains=search_keywords))
        pubDate = request.GET.get('pubDate', "")
        click_num = request.GET.get('click_num', "")
        if pubDate:
            policy = policy.order_by("-pubDate")
        if click_num:
            policy = policy.order_by("-click_num")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(policy, 15, request=request)
        policy_data = p.page(page)

        for policy_ in policy_data.object_list:
            policy_.has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=policy_.id, fav_type=0):
                    policy_.has_fav = True
        return render(request, 'policy-search.html', {
            'keywords': search_keywords,
            'pubDate': pubDate,
            'click_num': click_num,
            'policy': policy_data,
        })


class RecordTimeView(View):
    def get(self, request):
        policy = Policy.objects.order_by('-pubDate')[0]
        return HttpResponse(policy.pubDate, content_type='application/json')


class PolicyDetailView(View):
    def get(self, request, policy_id):
        # 此处的id为表默认为我们添加的值。
        policy = Policy.objects.get(policy_id=policy_id)
        # 增加政策点击数
        policy.click_num += 1
        policy.save()

        # 是否收藏
        has_fav_policy = False

        # 必须是用户已登录我们才需要判断。
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=policy.policy_id, fav_type=1):
        #         has_fav_policy = True
        return render(request, "policy-detail.html", {
            "policy": policy,
            "has_fav_policy": has_fav_policy,
        })


class PolicyBannerView(View):
    def get(self, request, banner_id):
        # 此处的id为表默认为我们添加的值。
        banner = Banner.objects.get(id=banner_id)
        # 增加政策点击数
        banner.click_num += 1
        banner.save()

        # 是否收藏
        has_fav_banner = False

        # 必须是用户已登录我们才需要判断。
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=banner.id, fav_type=1):
        #         has_fav_banner = True
        return render(request, "policy-banner.html", {
            "banner": banner,
            "has_fav_banner": has_fav_banner,
        })


class chartDataView(View):
    def get(self, request):
        all_chart = Chart.objects.all()
        chartData = all_chart.filter(tab=request.GET.get('tab', ''))
        if not chartData:
            return HttpResponse('{"status":"invalid"}', content_type='application/json')
        from django.core import serializers
        data = serializers.serialize("json", chartData)
        return HttpResponse(data, content_type='application/json')


class AddPolicyView(View):
    def post(self, request):
        province = Province.objects.filter(name=request.POST.get('addr', ''))
        if not province:
            province = Province(name=request.POST.get('addr', ''))
            province.save()
        province = Province.objects.get(name=request.POST.get('addr', ''))
        department = Department.objects.filter(name=request.POST.get('source', ''))
        if not department:
            department = Department(name=request.POST.get('source', ''))
            department.save()
        department = Department.objects.get(name=request.POST.get('source', ''))
        policy = Policy.objects.filter(policy_id=request.POST.get('policy_id', ''))
        if not policy:
            newPolicy = Policy(title=request.POST.get('title', ''), policy_id=request.POST.get('policy_id', ''),
                               addr=province, source=department, info=request.POST.get('info', ''),
                               pubDate=request.POST.get('pubDate', ''))
            newPolicy.save()
        return HttpResponse('{"status":"success"}', content_type='application/json')


class AddChartView(View):
    def post(self, request):
        chart = Chart.objects.filter(title=request.POST.get('title', ''))
        if not chart:
            chart_form = AddChartForm(request.POST)
            if chart_form.is_valid():
                new_chart = chart_form.save(commit=True)
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"invalid"}', content_type='application/json')
        return HttpResponse('{"status":"has exited"}', content_type='application/json')
