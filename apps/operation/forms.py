# _*_ coding: utf-8 _*_
from django import forms

from .models import SSDPatent, MessageBoard


# class AddPatentForm(forms.ModelForm):
#     class Meta:
#         model = SSDPatent
#         exclude = ['seller', 'if_success', 'click_num', 'fav_num', 'shop_status', 'add_time']


class AddOrderForm(forms.Form):
    order_name = forms.CharField(required=True)
    order_address = forms.CharField(required=True)
    order_contact = forms.CharField(required=True)
    order_mobile = forms.CharField(required=True, min_length=7, max_length=11)
    agree = forms.BooleanField(required=True)

class MessageBoardForm(forms.ModelForm):
    class Meta:
        model = MessageBoard
        exclude = ['user', 'add_time']