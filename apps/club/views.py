# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from operation.models import UserFavorite
from policy.models import Policy
from patent.models import Patent
from project.models import Project


# Create your views here.

class HomeView(View):
    def get(self, request):
        pass
