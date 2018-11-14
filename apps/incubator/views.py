from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.

from django.views.generic import View
from .models import Couveuse, Park, Financial


class ListView(View):
    def get(self, request):
        type_id = request.GET.get('type_id', '0')

        all_incubator = Couveuse.objects.all()
        if type_id == '1':
            all_incubator = Park.objects.all()
        if type_id == '2':
            all_incubator = Financial.objects.all()

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

        return render(request, 'incubator-list.html', {
            'type_id': type_id,
            'incubator': incubator,
            'area0': area0,
            'area1': area1,
            'area0s': area0s,
            'area1s': area1s
            # 'levels': levels,
            # 'types': types,
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
        return render(request, "incubator-detail.html", {
            "incubator": incubator,
        })
