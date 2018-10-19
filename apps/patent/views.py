# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Patent


# Create your views here.

class PatentView(View):
    def get(self, request):
        all_patent = Patent.objects.all()

        newest_patent = all_patent.order_by('-publish_time')[:3]

        patent_nums = all_patent.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_patent, 1, request=request)

        patent = p.page(page)

        return render(request, 'patent.html', {
            'all_patent': patent,
            'patent_nums': patent_nums,
            'newest_patent': newest_patent
        })
