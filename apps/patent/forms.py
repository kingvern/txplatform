# _*_ coding: utf-8 _*_
from django import forms

from DjangoUeditor.forms import UEditorField
from .models import Patent


class AddPatentForm(forms.ModelForm):
    detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
                          filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = Patent
        exclude = ['seller', 'hire', 'more_pic', 'click_num', 'fav_num', 'shop_status', 'add_time']


class ModifyPatentForm(forms.ModelForm):
    detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
                          filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = Patent
        exclude = ['seller', 'more_pic', 'hire', 'click_num', 'fav_num', 'shop_status', 'add_time']
