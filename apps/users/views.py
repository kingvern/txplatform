# _*_ encoding:utf-8 _*_
import json

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserFavorite, UserMessage, BuyerPatent, BuyerProject
from policy.models import Policy, Banner
from project.models import Project
from patent.models import Patent
from incubator.models import Couveuse, Park, Financial
from gallery.models import Gallery
from utils.id_card import checkIDNumber
from .models import UserProfile, VerifyCode, UpdateMobileRecord
from .forms import LoginForm, RegisterForm, ResetPwdForm, UpdateMobileForm, ModifyPwdForm, UploadImageForm, \
    UserInfoForm, UserAuthForm

from django.contrib.auth.mixins import LoginRequiredMixin

import re
import random
from txplatform.settings import APIKEY

from utils.yunpian import YunPian


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))
            # user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    """登录"""

    def get(self, request):
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_url = request.POST.get('next', '')
                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, 'login.html', {'msg': '邮箱未激活！'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ForCodeView(View):
    """获取手机验证码"""

    def post(self, request):
        mobile = request.POST.get('mobile', '')
        send_type = request.POST.get('send_type', 'register')
        if mobile:
            # 验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 生成手机验证码
                code = VerifyCode()
                code.mobile = mobile
                code.send_type = send_type
                c = random.randint(1000, 9999)
                code.code = str(c)
                code.save()
                code = VerifyCode.objects.filter(mobile=mobile).last().code
                yunpian = YunPian(APIKEY)
                sms_status = yunpian.send_sms(code=code, mobile=mobile)
                msg = sms_status
                return HttpResponse(msg)
            else:
                msg = '请输入有效手机号码!'
                return HttpResponse(msg)
        else:
            msg = '手机号不能为空！'
            return HttpResponse(msg)


class RegisterView(View):
    """注册"""

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            mobile = request.POST.get('mobile', '')
            if UserProfile.objects.filter(mobile=mobile):
                return render(request, 'register.html', {'msg': '该用户已经注册，请登录'})
            record = VerifyCode.objects.filter(
                Q(mobile=request.POST.get('mobile', '')) & Q(send_type='register')).last()
            if record:
                if record.code == request.POST.get('code', ''):
                    pwd1 = request.POST.get('password1', '')
                    pwd2 = request.POST.get('password2', '')
                    if pwd1 != pwd2:
                        return render(request, 'pwd_reset.html', {'mobile': mobile, 'msg': 'password not same'})
                    else:
                        pass_word = request.POST.get('password2', '')
                        user_profile = UserProfile()
                        user_profile.mobile = mobile
                        user_profile.is_active = True
                        user_profile.password = make_password(pass_word)
                        user_profile.save()
                    return render(request, 'login.html')
                else:
                    return HttpResponse(
                        '{"status":"fail", "msg":"验证码不一致"}',
                        content_type='application/json')
            return HttpResponse(
                '{"status":"fail", "msg":"请先获取验证码"}',
                content_type='application/json')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ResetPwdView(View):
    """重置密码"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        reset_pwd_form = ResetPwdForm()
        # mobile = request.user.mobile
        return render(request, 'reset_pwd.html', {'reset_pwd_form': reset_pwd_form})

    def post(self, request):
        reset_pwd_form = ResetPwdForm(request.POST)
        if reset_pwd_form.is_valid():
            mobile = request.POST.get('mobile', '')
            if not UserProfile.objects.filter(mobile=mobile):
                return render(request, 'register.html', {'msg': 'not registered'})
            record = VerifyCode.objects.filter(
                Q(mobile=request.POST.get('mobile', '')) & Q(send_type='reset_pwd')).last()
            if record:
                if record.code == request.POST.get('code', ''):
                    pwd1 = request.POST.get('password1', '')
                    pwd2 = request.POST.get('password2', '')
                    if pwd1 != pwd2:
                        return render(request, 'pwd_reset.html', {'mobile': mobile, 'msg': 'password not same'})
                    else:
                        user = UserProfile.objects.get(mobile=mobile)
                        user.password = make_password(pwd2)
                        user.save()
                        return render(request, 'login.html')
                else:
                    return HttpResponse(
                        '{"status":"fail", "msg":"cer code not same"}',
                        content_type='application/json')
            else:
                return HttpResponse(
                    '{"status":"fail", "msg":"get code first"}',
                    content_type='application/json')
        else:
            return render(request, 'reset_pwd.html', {'reset_pwd_form': reset_pwd_form})


class UpdateMobileView(LoginRequiredMixin, View):
    """更新手机号"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        modify_form = UpdateMobileForm()
        return render(request, 'update_mobile.html', {'update_mobile_form': modify_form})

    def post(self, request):
        modify_form = UpdateMobileForm(request.POST)
        if modify_form.is_valid():
            old_mobile = request.POST.get("old_mobile", "")
            new_mobile = request.POST.get("new_mobile", "")
            code = request.POST.get("code", "")

            user = request.user
            if old_mobile != user.mobile:
                return HttpResponse(
                    '{"status":"fail", "msg":"旧手机号不一致"}',
                    content_type='application/json')
            # 旧手机号一致
            record = VerifyCode.objects.filter(
                Q(mobile=request.POST.get('new_mobile', '')) & Q(send_type='update_mobile')).last()
            if record:
                if record.code == request.POST.get('code', ''):
                    user.mobile = new_mobile
                    user.username = new_mobile
                    # save保存到数据库
                    user.save()

                    record = UpdateMobileRecord()
                    record.old_mobile = old_mobile
                    record.new_mobile = new_mobile
                    record.code = code
                    record.save()
                    return HttpResponse(
                        '{"status":"success"}',
                        content_type='application/json')
                else:
                    return HttpResponse(
                        '{"status":"fail", "msg":"验证码不一致"}',
                        content_type='application/json')
            else:
                return HttpResponse(
                    '{"status":"fail", "msg":"请先获取验证码"}',
                    content_type='application/json')
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    modify_form.errors),
                content_type='application/json')


class UpdatePwdView(LoginRequiredMixin, View):
    """更新密码"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return HttpResponse(
                    '{"status":"fail", "msg":"密码不一致"}',
                    content_type='application/json')
            # 如果密码一致
            user = request.user
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        # 验证失败说明密码位数不够。
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    modify_form.errors),
                content_type='application/json')


class LogoutView(View):
    """登出"""

    def get(self, request):
        # django自带的logout
        logout(request)
        # 重定向到首页,
        return HttpResponseRedirect(reverse("index"))


class UserInfoView(LoginRequiredMixin, View):
    """用户中心"""

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        info_form = UserInfoForm(instance=request.user)
        return render(request, "usercenter-info.html", {
            'info_form': info_form
        })

    def post(self, request):
        # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
        info_form = UserInfoForm(request.POST, instance=request.user)
        if info_form.is_valid():
            # if user_info_form.username in list(UserProfile.objects.all().values_list('user_name')):
            #     return HttpResponse(
            #         '{"status":"fail","msg":"用户名重复，请更改"}',
            #         content_type='application/json')
            info_form.save()
            return HttpResponseRedirect(reverse('users:user_info'))
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return render(request, "usercenter-info.html", {
                'info_form': info_form
            })


class UserAuthView(LoginRequiredMixin, View):
    """用户认证"""

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        info_form = UserAuthForm(instance=request.user)
        auth = False
        if request.user.id_card:
            auth = True
        return render(request, "usercenter-auth.html", {
            'auth': auth,
            'info_form': info_form
        })

    def post(self, request):
        # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
        info_form = UserAuthForm(request.POST, instance=request.user)
        id_card = request.POST.get('id_card', '')
        res = checkIDNumber(id_card)
        if not res:
            auth = False
            return render(request, "usercenter-auth.html", {
                'auth': auth,
                'info_form': info_form,
                'msg': "id_card error"
            })
            # return HttpResponse(
            #     '{"status":"fail","msg":"id_card error"}',
            #     content_type='application/json')
        if info_form.is_valid():
            info_form.save()
            return HttpResponseRedirect(reverse('users:user_auth'))
        else:
            # 通过json的dumps方法把字典转换为json字符串
            auth = False
            return render(request, "usercenter-auth.html", {
                'auth': auth,
                'info_form': info_form
            })
            # return HttpResponse(
            #     json.dumps(
            #         user_info_form.errors),
            #     content_type='application/json')


# 用户上传图片的view:用于修改头像

class UploadImageView(LoginRequiredMixin, View):
    """更新图片"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request):
        # 这时候用户上传的文件就已经被保存到imageform了 ，为modelform添加instance值直接保存
        image_form = UploadImageForm(
            request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            # 取出cleaned data中的值,一个dict
            # avatar = image_form.cleaned_data['avatar']
            # request.user.avatar = avatar
            # request.user.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            return HttpResponse(
                '{"status":"fail"}',
                content_type='application/json')


# 个人中心页我的订单

class MyOrderView(LoginRequiredMixin, View):
    """我的订单"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        patent_order = BuyerPatent.objects.filter(buyer=request.user)
        project_order = BuyerProject.objects.filter(buyer=request.user)
        return render(request, "usercenter-myOrder.html", {
            "user_patent": patent_order,
            "user_project": project_order,
        })


class MySellOrderView(LoginRequiredMixin, View):
    """我卖出的订单"""

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        patent_order = BuyerPatent.objects.filter(patent__seller=request.user)
        project_order = BuyerProject.objects.filter(project__seller=request.user)
        return render(request, "usercenter-mySellOrder.html", {
            "user_patent": patent_order,
            "user_project": project_order,
        })


class MyPublishView(LoginRequiredMixin, View):
    """我的发布管理"""

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        patent_list = Patent.objects.filter(seller=request.user)
        project_list = Project.objects.filter(seller=request.user)
        return render(request, "usercenter-myPublish.html", {
            "patent_list": patent_list,
            "project_list": project_list
        })


# 我收藏的

class MyFavView(LoginRequiredMixin, View):
    """我的关注"""

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        patent_list = []
        patent_ids = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for patent_id in patent_ids:
            patent = Patent.objects.get(id=int(patent_id.fav_id))
            patent_list.append(patent)

        project_list = []
        project_ids = UserFavorite.objects.filter(user=request.user, fav_type=2)
        for project_id in project_ids:
            project = Project.objects.get(id=project_id.fav_id)
            project_list.append(project)

        return render(request, "usercenter-fav.html", {
            "patent_list": patent_list,
            "project_list": project_list
        })


class MyMessageView(LoginRequiredMixin, View):
    """我的信息"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)

        # 用户进入个人中心消息页面，清空未读消息记录
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_message, 4)
        messages = p.page(page)
        return render(request, "usercenter-message.html", {
            "messages": messages,
        })


class IndexView(View):
    """首页view"""

    def get(self, request):
        project = Project.objects.all().order_by('-click_num')[:6]
        bar_pic = Banner.objects.filter(if_toutiao=True)[:1][0]

        patent_bar = Patent.objects.all().order_by('-click_num')[:10]
        patent_0 = Patent.objects.all().filter(patent_category='fmzl')[:12]
        patent_1 = Patent.objects.all().filter(patent_category='syxxzl')[:12]
        patent_2 = Patent.objects.all().filter(patent_category='wgzl')[:12]

        policy = Policy.objects.order_by('-pubDate').filter(
            Q(source__if_show=True) & Q(addr__if_show=True) & Q(source_id='51'))[:10]

        return render(request, 'index.html', {
            "bar_pic": bar_pic,
            "patent_bar": patent_bar,
            "patent_0": patent_0,
            "patent_1": patent_1,
            "patent_2": patent_2,

            "project": project,

            "policy": policy
        })


class MyFavPolicyView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        policy_list = []
        ids = UserFavorite.objects.filter(user=request.user, fav_type=0)
        for id in ids:
            policy = Policy.objects.get(id=id.fav_id)
            policy_list.append(policy)
        return render(request, "usercenter-fav-policy.html", {
            "policy_list": policy_list
        })


class MyFavIncubatorView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        couveuse_list = []
        couveuse_ids = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for couveuse_id in couveuse_ids:
            couveuse = Couveuse.objects.get(id=int(couveuse_id.fav_id))
            couveuse_list.append(couveuse)
        park_list = []
        park_ids = UserFavorite.objects.filter(user=request.user, fav_type=4)
        for park_id in park_ids:
            park = Park.objects.get(id=int(park_id.fav_id))
            park_list.append(park)
        financial_list = []
        financial_ids = UserFavorite.objects.filter(user=request.user, fav_type=5)
        for financial_id in financial_ids:
            financial = Financial.objects.get(id=int(financial_id.fav_id))
            financial_list.append(financial)
        return render(request, "usercenter-fav-incubator.html", {
            "couveuse_list": couveuse_list,
            "park_list": park_list,
            "financial_list": financial_list
        })


class MyFavGalleryView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        gallery_list = []
        gallery_ids = UserFavorite.objects.filter(user=request.user, fav_type=6)
        for gallery_id in gallery_ids:
            gallery = Gallery.objects.get(id=gallery_id.fav_id)
            gallery_list.append(gallery)
        return render(request, "usercenter-fav-gallery.html", {
            "gallery_list": gallery_list
        })


class AgreementView(View):
    def get(self, request):
        return render(request, "agreement.html", {})
