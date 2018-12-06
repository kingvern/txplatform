# _*_ coding: utf-8 _*_
import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect

from .models import Patent
from operation.models import UserFavorite, UserJoin, BuyerPatent, BuyerProject
from policy.models import Policy
from patent.models import Patent
from project.models import Project
from incubator.models import Couveuse, Park, Financial
from gallery.models import Gallery
from .forms import AddOrderForm
from users.models import UserProfile
from platorm.settings import APIKEY


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
        if not request.user.is_authenticated():
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

            elif int(type) == 3:
                project = Couveuse.objects.get(id=int(id))
                project.fav_num -= 1
                if project.fav_num < 0:
                    project.fav_num = 0
                project.save()
            elif int(type) == 4:
                project = Park.objects.get(id=int(id))
                project.fav_num -= 1
                if project.fav_num < 0:
                    project.fav_num = 0
                project.save()
            elif int(type) == 5:
                project = Financial.objects.get(id=int(id))
                project.fav_num -= 1
                if project.fav_num < 0:
                    project.fav_num = 0
                project.save()
            elif int(type) == 6:
                project = Gallery.objects.get(id=int(id))
                project.fav_num -= 1
                if project.fav_num < 0:
                    project.fav_num = 0
                project.save()

            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            # 过滤掉未取到fav_id type的默认情况
            if int(type) >= 0 and int(id) >= 0:
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
                if int(type) == 2:
                    project = Project.objects.get(id=int(id))
                    project.fav_num += 1
                    project.save()

                if int(type) == 3:
                    policy = Couveuse.objects.get(id=int(id))
                    policy.fav_num += 1
                    policy.save()
                if int(type) == 4:
                    patent = Park.objects.get(id=int(id))
                    patent.fav_num += 1
                    patent.save()
                if int(type) == 5:
                    project = Financial.objects.get(id=int(id))
                    project.fav_num += 1
                    project.save()
                if int(type) == 6:
                    project = Gallery.objects.get(id=int(id))
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
        if not request.user.is_authenticated():
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


class CancelPublishView(View):
    """
    下架和重新上架功能
    """

    def post(self, request):
        id = request.POST.get('id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('type', 0)

        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        if int(type) == 1:
            patent = Patent.objects.get(id=int(id))
            if patent.shop_status != '-1':
                patent.shop_status = '-1'
                patent.if_show = False
                patent.save()
                return HttpResponse('{"status":"success", "msg":"上架"}', content_type='application/json')
            elif patent.shop_status == '-1':
                patent.shop_status = '0'
                patent.if_show = True
                patent.save()
                return HttpResponse('{"status":"success", "msg":"下架"}', content_type='application/json')
        elif int(type) == 2:
            patent = Project.objects.get(id=int(id))
            if patent.shop_status != '-1':
                patent.shop_status = '-1'
                patent.if_show = False
                patent.save()
                return HttpResponse('{"status":"success", "msg":"上架"}', content_type='application/json')
            elif patent.shop_status == '-1':
                patent.shop_status = '0'
                patent.if_show = True
                patent.save()
                return HttpResponse('{"status":"success", "msg":"下架"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"下架出错"}', content_type='application/json')


class DeletePublishView(View):
    """
    删除功能
    """

    def post(self, request):
        # 表明你收藏的不管是课程，讲师，还是机构。他们的id
        # 默认值取0是因为空串转int报错
        id = request.POST.get('id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('type', 0)

        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        if int(type) == 1:
            patent = Patent.objects.get(id=int(id))
            patent.delete()
            return HttpResponse('{"status":"success", "msg":"已经删除"}', content_type='application/json')

        elif int(type) == 2:
            project = Project.objects.get(id=int(id))
            project.delete()
            return HttpResponse('{"status":"success", "msg":"已经删除"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"删除出错"}', content_type='application/json')


class OrderView(View):
    """
    下单功能
    type 1:下单
    type 2:删除订单
    type 3:无意义
    """

    def get(self, request):
        id = request.GET.get('id', 0)
        if int(id) > 0:
            patent = Patent.objects.get(id=int(id))
            exist_records = BuyerPatent.objects.filter(buyer=request.user, patent=patent, step__in=['0', '1', '2', '3'])
            if exist_records:
                exist_record = exist_records[0]
                if exist_record.step == '0':
                    # 下单未付款
                    from platorm.settings import NAME, ADDRESS, CONTACT, MOBILE
                    return render(request, 'pay_order.html', {
                        'order': exist_record
                    })
            from platorm.settings import NAME, ADDRESS, CONTACT, MOBILE
            return render(request, 'add_order.html', {
                'patent': patent,
                'NAME': NAME,
                'ADDRESS': ADDRESS,
                'CONTACT': CONTACT,
                'MOBILE': MOBILE
            })
        else:
            return HttpResponseRedirect(reverse('patent:list'))

    def post(self, request):
        id = request.POST.get('id', 0)
        type = request.POST.get('type', 1)
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        if int(type) == 1:
            if int(type) == 1 and int(id) > 0:
                add_order_form = AddOrderForm(request.POST)
                if add_order_form.is_valid():
                    order = BuyerPatent()
                    patent = Patent.objects.get(id=int(id))

                    order.buyer = request.user
                    order.patent = patent
                    patent.if_show = False
                    patent.save()

                    order.order_name = request.POST.get('order_name', '')
                    order.order_address = request.POST.get('order_address', '')
                    order.order_contact = request.POST.get('order_contact', '')
                    order.order_mobile = request.POST.get('order_mobile', '')

                    order.base_price = patent.price
                    order.serve_fee = patent.hire
                    order.total_price = patent.hire + patent.price
                    order.step = '0'
                    order.save()
                # return HttpResponse('{"status":"success", "msg":"已经下单"}', content_type='application/json')
                # staff = UserProfile.objects.filter(is_staff=True).order_by()
                # return render(request, 'pay_order.html', {'order': order})
                return HttpResponseRedirect("/operation/add_order/?id=" + id)
            else:
                return HttpResponseRedirect(reverse('patent:list'))
            # else:
            # return render(request, 'login.html', {'login_form': login_form})

        elif int(type) == 2:
            order = BuyerProject.objects.get(id=int(id))
            order.delete()
            return HttpResponse('{"status":"success", "msg":"已经删除"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"删除出错"}', content_type='application/json')


class CancelOrderView(View):
    """
    取消订单
    """

    def post(self, request):
        id = request.POST.get('id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('type', 0)

        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        if int(type) == 1:
            order = BuyerPatent.objects.get(id=int(id))
            order.step = '-1'
            order.step_time = datetime.datetime.now()
            order.save()
            return HttpResponse('{"status":"success", "msg":"上架"}', content_type='application/json')
        elif int(type) == 2:
            project = Project.objects.get(id=int(id))
            project.shop_status = '-1'
            project.if_show = False
            project.save()
            return HttpResponse('{"status":"success", "msg":"已经下架"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"下架出错"}', content_type='application/json')


class DeleteOrderView(View):
    """
    删除功能
    """

    def post(self, request):
        # 表明你收藏的不管是课程，讲师，还是机构。他们的id
        # 默认值取0是因为空串转int报错
        id = request.POST.get('id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('type', 0)

        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        if int(type) == 1:
            order = BuyerPatent.objects.get(id=int(id))
            order.delete()
            return HttpResponse('{"status":"success", "msg":"已经删除"}', content_type='application/json')

        elif int(type) == 2:
            order = BuyerProject.objects.get(id=int(id))
            order.delete()
            return HttpResponse('{"status":"success", "msg":"已经删除"}', content_type='application/json')

        else:
            return HttpResponse('{"status":"fail", "msg":"删除出错"}', content_type='application/json')


class AskView(View):
    """
    咨询功能
    """

    def post(self, request):
        id = request.POST.get('id', 0)
        # 取到你收藏的类别，从前台提交的ajax请求中取
        type = request.POST.get('type', 0)

        # 收藏与已收藏取消收藏
        # 判断用户是否登录:即使没登录会有一个匿名的user
        if not request.user.is_authenticated():
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserJoin.objects.filter(user=request.user, id=int(id), type=int(type))
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
