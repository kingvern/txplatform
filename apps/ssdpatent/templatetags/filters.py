import json

from django.template import Library

register = Library()

#一个偶数为真的过滤器
@register.filter
def static_imgo(imgo):
    if not imgo.url:
        return False
    else:
        return imgo.url[:4] != 'http'

@register.filter
def filter_imgo(imgo):
    # return imgo
    return imgo[:11] != '/media/http'


