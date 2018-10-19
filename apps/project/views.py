# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Project


# Create your views here.

class ProjectView(View):
    def get(self, request):
        all_project = Project.objects.all()

        newest_project = all_project.order_by('-publish_time')[:3]

        project_nums = all_project.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_project, 1, request=request)

        project = p.page(page)

        return render(request, 'project.html', {
            'all_project': project,
            'project_nums': project_nums,
            'newest_project': newest_project
        })
