# _*_ coding: utf-8 _*_
from django import forms

from captcha.fields import CaptchaField

from users.models import UserProfile, UpdateMobileRecord


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    mobile = forms.CharField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
    code = forms.CharField(required=True)


class ResetPwdForm(forms.Form):
    mobile = forms.CharField(required=True)
    code = forms.CharField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class UpdateMobileForm(forms.Form):
    old_mobile = forms.CharField(required=True)
    code = forms.CharField(required=True)
    new_mobile = forms.CharField(required=True)


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)


# 用于文件上传，修改头像
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'gender', 'birthday',  'mobile']


class UserAuthForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'id_card']
