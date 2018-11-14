# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Patent
from operation.models import UserFavorite, UserJoin
from policy.models import Policy
from patent.models import Patent
from project.models import Project
from gallery.models import Gallery


# Create your views here.

class AddFavView(View):
    """
    用户收藏与取消收藏功能
    """

    def post(self, request):
        # 表明你收藏的不管是课程，讲师，还是机构。他们的id
        # 默认值取0是因为空串转int报错
        id = request.POST.get('fav_id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('fav_type', 0)

        # 收藏与已收藏取消收藏
        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated:
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(id), fav_type=int(type))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            if int(type) == 0:
                policy = Policy.objects.get(id=int(id))
                policy.fav_num -= 1
                if policy.fav_num < 0:
                    policy.fav_num = 0
                policy.save()
            if int(type) == 1:
                patent = Patent.objects.get(id=int(id))
                patent.fav_num -= 1
                if patent.fav_num < 0:
                    patent.fav_num = 0
                patent.save()
            elif int(type) == 2:
                project = Project.objects.get(id=int(id))
                project.fav_num -= 1
                if project.fav_num < 0:
                    project.fav_num = 0
                project.save()

            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            # 过滤掉未取到fav_id type的默认情况
            if int(type) > 0 and int(id) > 0:
                user_fav.fav_id = int(id)
                user_fav.fav_type = int(type)
                user_fav.user = request.user
                user_fav.save()

                if int(type) == 0:
                    policy = Policy.objects.get(id=int(id))
                    policy.fav_num += 1
                    policy.save()
                if int(type) == 1:
                    patent = Patent.objects.get(id=int(id))
                    patent.fav_num += 1
                    patent.save()
                elif int(type) == 2:
                    project = Project.objects.get(id=int(id))
                    project.fav_num += 1
                    project.save()
                return HttpResponse('{"status":"success", "msg":"取消收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')


class AddJoinView(View):
    """
    用户报名与取消报名功能
    """

    def post(self, request):
        id = request.POST.get('join_id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('join_type', 0)

        # 收藏与已收藏取消收藏
        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated:
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserJoin.objects.filter(user=request.user, join_id=int(id), join_type=int(type))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消收藏
            gallery = Gallery.objects.get(id=int(id))
            gallery.join_num -= 1
            if gallery.join_num < 0:
                gallery.join_num = 0
            gallery.save()

            return HttpResponse('{"status":"success", "msg":"报名"}', content_type='application/json')
        else:
            user_join = UserJoin()
            # 过滤掉未取到join_id type的默认情况
            if int(type) > 0 and int(id) > 0:
                user_join.join_id = int(id)
                user_join.join_type = int(type)
                user_join.user = request.user
                user_join.save()

                gallery = Gallery.objects.get(id=int(id))
                gallery.join_num += 1
                gallery.save()
                return HttpResponse('{"status":"success", "msg":"取消报名"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"报名出错"}', content_type='application/json')
