# _*_ coding: utf-8 _*_
from django import forms

from .models import Member


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['user', 'status', 'note', 'add_time']
