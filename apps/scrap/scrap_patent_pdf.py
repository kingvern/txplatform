# _*_ coding: utf-8 _*_

# 通过在发送post请求时添加一个data参数，这个data参数可以通过字典构造成
import requests
import json
import time

# from multiprocessing import Pool

patent_list_with_pdf = []
cnt = 0


def searchData(patent):
    global patent_list_with_pdf
    global cnt
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    get_url = 'http://114.251.8.193/api/patent/download?client_id=2aeb5a5eac1100043817950ada19e0f5&access_token=95b02c41-0003-4733-b0b1-e73ab728e5cf&scope=read_cn&pid='

    # response = requests.post(url, data=data)
    response = s.get(get_url + patent['pid'])
    jsonData = ''
    cnt += 1
    print(str(cnt) + '/675')
    # print(patent['pid'])
    try:
        jsonData = json.loads(response.text)
    except:
        print(response.text)
        print("jsonData error")
        with open('patent_list_with_pdf.json', 'w+') as file_obj:
            json.dump(patent_list_with_pdf, file_obj)
        return
    patent['pdf'] = 'http://' + jsonData['context']['records'][0]['nginxPath']
    patent_list_with_pdf.append(patent)
    # print(patent)
    # print(patent_list_with_pdf)


def scrap_datas(patent_list):
    print('START')

    # agents = 5
    # chunksize = 3
    # with Pool(processes=agents) as pool:
    #     pool.map(searchData, addrs, chunksize)

    for patent in patent_list:
        searchData(patent)
    print('END')


if __name__ == '__main__':
    patent_list = []
    with open('patent_list.json', 'r') as file_obj:
        patent_list = json.load(file_obj)
    print(len(patent_list))
    # searchData(patent_list[0])
    # searchData(patent_list[1])
    # searchData(patent_list[2])

    scrap_datas(patent_list)

    with open('patent_list_with_pdf.json', 'w+') as file_obj:
        json.dump(patent_list_with_pdf, file_obj)
