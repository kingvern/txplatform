from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.

from django.views.generic import View
from .models import Couveuse, Park, Financial, YellowPage
from operation.models import UserFavorite


class ListView(View):
    def get(self, request):
        type_id = request.GET.get('type_id', '0')

        all_incubator = Couveuse.objects.all()
        if type_id == '1':
            all_incubator = Park.objects.all()
        if type_id == '2':
            all_incubator = Financial.objects.all()
        if type_id == '3':
            all_incubator = YellowPage.objects.all()

        area0 = request.GET.get('area0', '')
        area1 = request.GET.get('area1', '')

        area0s = all_incubator.values('area0').distinct()
        # levels = all_incubator.values('level').distinct()
        # types = all_incubator.values('type').distinct()

        if area0:
            all_incubator = all_incubator.filter(area0=area0)

        area1s = all_incubator.values('area1').distinct()
        if area1:
            all_incubator = all_incubator.filter(area1=area1)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_incubator, 10, request=request)

        incubator = p.page(page)

        recommend_couveuse = Couveuse.objects.filter(if_recommend=True)[:3]
        recommend_park = Park.objects.filter(if_recommend=True)[:3]
        recommend_financial = Financial.objects.filter(if_recommend=True)[:3]

        for policy_ in incubator.object_list:
            policy_.has_fav = False
            if request.user.is_authenticated():
                if type_id == '0':
                    if UserFavorite.objects.filter(user=request.user, fav_id=policy_.id, fav_type=3):
                        policy_.has_fav = True
                if type_id == '1':
                    if UserFavorite.objects.filter(user=request.user, fav_id=policy_.id, fav_type=4):
                        policy_.has_fav = True
                if type_id == '2':
                    if UserFavorite.objects.filter(user=request.user, fav_id=policy_.id, fav_type=5):
                        policy_.has_fav = True
        return render(request, 'incubator-list.html', {
            'type_id': type_id,
            'incubator': incubator,
            'area0': area0,
            'area1': area1,
            'area0s': area0s,
            'area1s': area1s,
            "recommend_couveuse": recommend_couveuse,
            "recommend_park": recommend_park,
            "recommend_financial": recommend_financial,

            # 'levels': levels,
            # 'types': types,
        })


class SearchView(View):
    def get(self, request):
        project = Couveuse.objects.all()
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            project = project.filter(Q(name__icontains=search_keywords) | Q(detail__icontains=search_keywords))
        pubDate = request.GET.get('pubDate', "")
        click_num = request.GET.get('click_num', "")
        if pubDate:
            project = project.order_by("-pubDate")
        if click_num:
            project = project.order_by("-click_num")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(project, 15, request=request)
        project_data = p.page(page)

        for project_ in project_data.object_list:
            project_.has_fav = False
            if request.user.is_authenticated():
                if UserFavorite.objects.filter(user=request.user, fav_id=project_.id, fav_type=0):
                    project_.has_fav = True
        return render(request, 'project-search.html', {
            'keywords': search_keywords,
            'pubDate': pubDate,
            'click_num': click_num,
            'all_project': project_data,
        })


class DetailView(View):
    def get(self, request, incubator_id):
        type_id = request.GET.get('type_id', '0')
        if type_id == '0':
            incubator = Couveuse.objects.get(id=int(incubator_id))
        if type_id == '1':
            incubator = Park.objects.get(id=int(incubator_id))
        if type_id == '2':
            incubator = Financial.objects.get(id=int(incubator_id))
        if type_id == '3':
            incubator = YellowPage.objects.get(id= int(incubator_id))
        return render(request, "incubator-detail.html", {
            "incubator": incubator,
        })
