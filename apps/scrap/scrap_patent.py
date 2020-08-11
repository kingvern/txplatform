# _*_ coding: utf-8 _*_

# 通过在发送post请求时添加一个data参数，这个data参数可以通过字典构造成
import requests
import json
import time


# from multiprocessing import Pool

patent_list = []

def searchData(i):
    global patent_list
    # url = "http://114.251.8.193/api/patent/search/expression"
    # data = {
    #     "client_id": '2aeb5a5eac1100043817950ada19e0f5',
    #     "access_token": '95b02c41-0003-4733-b0b1-e73ab728e5cf',
    #     "scope": "read_cn",
    #     'express': '相关权利人=首都师范大学 AND LSSCN=有权,在审',
    #     "page": i
    # }
    # url = "http://114.251.8.193/oauth/authorize"
    # data = {
    #     "client_id": '2aeb5a5eac1100043817950ada19e0f5',
    #     "redirect_uri": 'http://39.100.199.59/',
    #     "scope": "read_cn",
    #     'response_type': 'code'
    # }
    get_url = 'http://114.251.8.193/api/patent/search/expression?client_id=2aeb5a5eac1100043817950ada19e0f5&access_token=95b02c41-0003-4733-b0b1-e73ab728e5cf&scope=read_cn&express=%E7%9B%B8%E5%85%B3%E6%9D%83%E5%88%A9%E4%BA%BA%3D%E9%A6%96%E9%83%BD%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6%20AND%20LSSCN%3D%E6%9C%89%E6%9D%83&page='

    # response = requests.post(url, data=data)
    response = requests.get(get_url + str(i))
    jsonData = ''
    print(i)
    try:
        jsonData = json.loads(response.text)
    except:
        print(response.text)
        print("jsonData error")
        return
    patent_list += jsonData['context']['records']
    # print(jsonData)


def is_valid_date(str):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False


def compare_time(time1, time2):
    s_time = time.mktime(time.strptime(time1, '%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2, '%Y-%m-%d'))
    return int(s_time) - int(e_time)


def scrap_datas():
    print('START')

    print('nowTime: ' + time.strftime('%Y-%m-%d', time.localtime(time.time())))

    # agents = 5
    # chunksize = 3
    # with Pool(processes=agents) as pool:
    #     pool.map(searchData, addrs, chunksize)

    for i in range(1, 69):
        searchData(i)
    print('END')


def test():
    with open('a.txt', 'w') as f:
        f.write('Hello, world!')
    print('')
    return 1


if __name__ == '__main__':
    scrap_datas()
    # searchData(1)
    print(patent_list)
    with open('patent_list.json','w+') as file_obj:
        json.dump(patent_list,file_obj)
