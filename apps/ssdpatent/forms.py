# _*_ coding: utf-8 _*_
from django import forms

from DjangoUeditor.forms import UEditorField
from .models import SSDPatent




class AddSSDPatentForm(forms.ModelForm):
    # detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
    #                       filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    # CATEGORY_LIST = (('0', '未分类'), ('1', '太赫兹'), ('2', '遥感成像'), ('3', '高可靠嵌入式'), ('4', '智能识别'),
    #                  ('5', '化学化工'), ('6', '新能源'), ('7', '机械'), ('8', '环保和资源'), ('9', '交通运输'),
    #                  ('21', '教育'), ('11', '仪器仪表'), ('12', '新型材料'), ('13', '电子信息'),
    #                  ('14', '生物科学'), ('15', '农林牧业'),
    #                  ('19', '电气自动化'),
    #                  ('23', '安全防护'))
    # category = forms.CharField(widget=forms.Select(choices=CATEGORY_LIST))
    class Meta:
        model = SSDPatent
        exclude = ['seller',  'click_num', 'fav_num', 'shop_status', 'add_time', 'if_show', 'if_success']


class ModifySSDPatentForm(forms.ModelForm):
    # detail = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/",
    #                       filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={})
    # CATEGORY_LIST = (('0', '未分类'), ('1', '太赫兹'), ('2', '遥感成像'), ('3', '高可靠嵌入式'), ('4', '智能识别'),
    #                  ('5', '化学化工'), ('6', '新能源'), ('7', '机械'), ('8', '环保和资源'), ('9', '交通运输'),
    #                  ('21', '教育'), ('11', '仪器仪表'), ('12', '新型材料'), ('13', '电子信息'),
    #                  ('14', '生物科学'), ('15', '农林牧业'),
    #                  ('19', '电气自动化'),
    #                  ('23', '安全防护'))
    # category = forms.CharField(widget=forms.Select(choices=CATEGORY_LIST))
    class Meta:
        model = SSDPatent
        exclude = ['seller',  'click_num', 'fav_num', 'shop_status', 'add_time', 'if_show', 'if_success']
