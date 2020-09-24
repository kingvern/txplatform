# _*_ coding: utf-8 _*_
import json
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

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

class BannerDetailView(View):
    def get(self, request, banner_id):
        banner = Banner.objects.get(id=int(banner_id))

        return render(request, "club-banner-detail.html", {
            "banner": banner
        })

class AddMemberView(LoginRequiredMixin, View):
    def get(self, request):
        add_member_form = AddMemberForm(instance=request.user)
        return render(request, "club-join.html", {
            'add_member_form':add_member_form
        })

    def post(self, request):
        add_member_form = AddMemberForm(request.POST, request.FILES, instance=request.user)
        if add_member_form.is_valid():
            member = add_member_form.save(commit=False)
            member.user = request.user
            member.save()
            return HttpResponseRedirect(reverse('club:home'))
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return render(request, "club-join.html", {
                'add_member_form': add_member_form
            })
