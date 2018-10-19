# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Policy, Department, Province

from .forms import UserAskForm


# Create your views here.

class PolicyView(View):
    def get(self, request):
        all_policy = Policy.objects.all()
        all_department = Department.objects.all()
        all_province = Province.objects.all()

        newest_policy = all_policy.order_by('-publish_time')[:3]

        province_id = request.GET.get('province', '')
        if province_id:
            all_policy = all_policy.filter(Province_id=int(province_id))
        department_id = request.GET.get('department', '')
        if department_id:
            all_policy = all_policy.filter(Department_id=int(department_id))

        policy_nums = all_policy.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_policy, 1, request=request)

        policy = p.page(page)

        return render(request, 'policy.html', {
            'all_policy': policy,
            'all_department': all_department,
            'all_province': all_province,
            'policy_nums': policy_nums,
            'department_id': department_id,
            'newest_policy': newest_policy
        })


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors), content_type='application/json')
