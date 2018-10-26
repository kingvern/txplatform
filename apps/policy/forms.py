# _*_ coding: utf-8 _*_

from django import forms

from operation.models import UserAsk
from .models import Policy, Chart


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'policy_name']


class AddPolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['policy_id', 'title', 'addr', 'source', 'pubDate', 'info']


class AddChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ['tab', 'tab2', 'title', 'data']
