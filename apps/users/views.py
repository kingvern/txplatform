# _*_ encoding:utf-8 _*_
import json

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserFavorite, UserMessage, BuyerPatent, BuyerProject
from project.models import Project
from patent.models import Patent
from .models import UserProfile, EmailVerifyRecord, VerifyCode, UpdateMobileRecord
from .forms import LoginForm, RegisterForm, ResetPwdForm, UpdateMobileForm, ModifyPwdForm, UploadImageForm, \
    UserInfoForm, UserAuthForm
from utils.email_send import send_register_email

from django.contrib.auth.mixins import LoginRequiredMixin

import re
import random
from platorm.settings import APIKEY

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
                    return render(request, 'index.html')
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
                msg = sms_status.msg
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
                    pass_word = request.POST.get('password', '')
                    user_profile = UserProfile()
                    user_profile.username = mobile
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
        return render(request, 'reset_pwd.html', {'reset_pwd_form': reset_pwd_form})

    def post(self, request):
        reset_pwd_form = ResetPwdForm(request.POST)
        if reset_pwd_form.is_valid():
            mobile = request.POST.get('mobile', '')
            if not UserProfile.objects.filter(mobile=mobile):
                return render(request, 'register.html', {'msg': '该用户未注册，请注册'})
            record = VerifyCode.objects.filter(
                Q(mobile=request.POST.get('mobile', '')) & Q(send_type='reset_pwd')).last()
            if record:
                if record.code == request.POST.get('code', ''):
                    pwd1 = request.POST.get('password1', '')
                    pwd2 = request.POST.get('password2', '')
                    if pwd1 != pwd2:
                        return render(request, 'pwd_reset.html', {'mobile': mobile, 'msg': '密码不一致'})
                    else:
                        user = UserProfile.objects.get(mobile=mobile)
                        user.password = make_password(pwd2)
                        user.save()
                        return render(request, 'login.html')
                else:
                    return HttpResponse(
                        '{"status":"fail", "msg":"验证码不一致"}',
                        content_type='application/json')
            else:
                return HttpResponse(
                    '{"status":"fail", "msg":"请先获取验证码"}',
                    content_type='application/json')
        else:
            return render(request, 'reset_pwd.html', {'reset_pwd_form': reset_pwd_form})


class UpdateMobileView(LoginRequiredMixin, View):
    """更新手机号"""

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

    def get(self, request):
        return render(request, "usercenter-info.html", {
        })

    def post(self, request):
        # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    user_info_form.errors),
                content_type='application/json')


class UserAuthView(LoginRequiredMixin, View):
    """用户认证"""

    def get(self, request):
        return render(request, "usercenter-auth.html", {
        })

    def post(self, request):
        # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
        user_info_form = UserAuthForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    user_info_form.errors),
                content_type='application/json')


class UserPublishView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "usercenter-publish.html", {
        })


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
        user_patent = BuyerPatent.objects.filter(buyer=request.user)
        user_project = BuyerProject.objects.filter(buyer=request.user)
        return render(request, "usercenter-myorder.html", {
            "user_patent": user_patent,
            "user_project": user_project,
        })


# 我收藏的

class MyFavView(LoginRequiredMixin, View):
    """我的收藏"""
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        patent_list = []
        patent_ids = UserFavorite.objects.filter(user=request.user, fav_type=0)
        for patent_id in patent_ids:
            patent = Patent.objects.get(id=patent_id)
            patent_list.append(patent)

        project_list = []
        project_ids = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for project_id in project_ids:
            project = Project.objects.get(id=project_id)
            project_list.append(project)

        return render(request, "usercenter-fav.html", {
            "patent_list": patent_list,
            "project_list": project_list
        })


class MyPublishView(LoginRequiredMixin, View):
    """我的发布管理"""

    def get(self, request):
        patent_list = Patent.objects.filter(seller=request.user)
        project_list = Project.objects.filter(seller=request.user)

        return render(request, "usercenter-myPublish.html", {
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
        project = Project.objects.all().order_by('index')[:5]
        # 正常位课程
        patent = Patent.objects.filter(is_banner=False)[:6]
        return render(request, 'index.html', {
            "project": project,
            "patent": patent,
        })
