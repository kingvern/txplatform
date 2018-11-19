# _*_ coding: utf-8 _*_
from django import forms

from .models import Patent


class AddPatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        exclude = ['seller', 'hire', 'more_pic', 'click_num', 'fav_num', 'shop_status', 'add_time']


class ModifyPatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        exclude = ['seller', 'more_pic','hire', 'click_num', 'fav_num', 'shop_status', 'add_time']
