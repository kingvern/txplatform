# _*_ coding: utf-8 _*_
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from club.models import Banner, Section, Member, Resource
from .forms import AddMemberForm


# Create your views here.

class HomeView(View):
    def get(self, request):
        all_banner = Banner.objects.all()
        all_section = Section.objects.all()
        all_member = Member.objects.all()
        all_resource = Resource.objects.all()

        return render(request, 'club-home.html', {
            'all_banner': all_banner,
            'all_section': all_section,
            'all_member': all_member,
            'all_resource': all_resource
        })


class DetailView(View):
    def get(self, request, section_id):
        section = Section.objects.get(id=int(section_id))

        return render(request, "club-detail.html", {
            "section": section
        })


class AddMemberView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "club-join.html", {

        })

    def post(self, request):
        add_member_form = AddMemberForm(request.POST, request.FILES, )
        if add_member_form.is_valid():
            member = add_member_form.save(commit=False)
            member.user = request.user
            member.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    add_member_form.errors),
                content_type='application/json')
