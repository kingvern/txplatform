# _*_ coding: utf-8 _*_
from django import forms

from DjangoUeditor.forms import UEditorField
from .models import Project


class AddProjectForm(forms.ModelForm):
    detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
                          filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = Project
        exclude = ['seller', 'price', 'shop_status', 'bargain', 'hire', 'click_num', 'fav_num', 'add_time']


class ModifyProjectForm(forms.ModelForm):
    detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
                          filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = Project
        exclude = ['seller', 'price', 'shop_status', 'bargain', 'hire', 'click_num', 'fav_num', 'add_time']
