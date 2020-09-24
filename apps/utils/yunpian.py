# _*_ coding: utf-8 _*_

import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【闪电树懒科技】您的验证码是{code}'.format(code=code)
            # 'text': '【王远欣】您的验证码是{code}'.format(code=code)
        }
        # text必须要跟云片后台的模板内容 保持一致，不然发送不出去！
        r = requests.post(self.single_send_url, data=parmas)
        print(r)
        return '发送成功！'


if __name__ == '__main__':
    yun_pian = YunPian('460b7e12332b41a211c21ab4dd4b6481')
    yun_pian.send_sms('123456', '18801272770')
