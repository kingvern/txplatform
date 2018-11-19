# _*_ coding: utf-8 _*_
from django import forms

from .models import Project


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['seller', 'price', 'shop_status', 'bargain', 'hire', 'click_num', 'fav_num', 'add_time']


class ModifyProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['seller', 'price', 'shop_status', 'bargain', 'hire', 'click_num', 'fav_num', 'add_time']
