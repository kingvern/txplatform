# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Patent
from operation.models import UserFavorite

# Create your views here.

class PatentListView(View):
    def get(self, request):
        all_patent = Patent.objects.all()
        field_category = request.GET.get('field_category', '')
        patent_category = request.GET.get('patent_category', '')
        price_down = request.GET.get('price_down', '')
        price_up = request.GET.get('price_up', '')

        if field_category:
            all_patent = all_patent.filter(field_category=field_category)
        if patent_category:
            all_patent = all_patent.filter(patent_category=patent_category)
        if price_down:
            all_patent = all_patent.filter(price__gte=price_down)
        if price_up:
            all_patent = all_patent.filter(price__lte=price_up)

        patent_nums = all_patent.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_patent, 1, request=request)

        patent = p.page(page)

        return render(request, 'patent-list.html', {
            'all_patent': patent,
            'patent_nums': patent_nums,
            'field_category': field_category,
            'patent_category': patent_category,
            'price_down': price_down,
            'price_up': price_up
        })
    
class PatentDetailView(View):
    def get(self, request, patent_id):
        # 此处的id为表默认为我们添加的值。
        patent = Patent.objects.get(id = int(patent_id))
        # 增加专利点击数
        # patent.click_nums += 1
        patent.save()

        # 是否收藏
        has_fav_patent = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=patent.id, fav_type=1):
                has_fav_patent = True
        # 取出标签找到标签相同的patent
        keyword = patent.keyword
        if keyword:
            # 从1开始否则会推荐自己
            relate_patents = Patent.objects.filter(keyword=keyword)[1:2]
        else:
            relate_patents = []
        return  render(request, "patent-detail.html", {
            "patent":patent,
            "relate_patents":relate_patents,
            "has_fav_patent":has_fav_patent,
        })