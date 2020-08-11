# _*_ coding: utf-8 _*_
from django import forms

from DjangoUeditor.forms import UEditorField
from .models import SSDPatent


class AddSSDPatentForm(forms.ModelForm):
    # detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
    #                       filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = SSDPatent
        exclude = ['seller',  'click_num', 'fav_num', 'shop_status', 'add_time', 'if_show', 'if_success']


class ModifySSDPatentForm(forms.ModelForm):
    # detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
    #                       filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    class Meta:
        model = SSDPatent
        exclude = ['seller',  'click_num', 'fav_num', 'shop_status', 'add_time', 'if_show', 'if_success']
