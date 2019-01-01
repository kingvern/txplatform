# _*_ coding: utf-8 _*_

# 通过在发送post请求时添加一个data参数，这个data参数可以通过字典构造成
import requests
import json
import time


def searchData(addr, recordTimeStr):
    url = "http://www.bayuegua.com/granoti/listCrossNew"
    pageSize = "100"
    data = {
        "addr": addr,
        "pageSize": pageSize,
        "pageNum": "1"
    }
    response = requests.post(url, data=data)
    jsonData = json.loads(response.text)
    print(jsonData["pages"])
    pages = jsonData["pages"]
    n = 0
    for i in range(pages):
        print('pageNum', i + 1)
        data = {
            "addr": addr,
            "pageSize": pageSize,
            "pageNum": i + 1
        }
        response = requests.post(url, data=data)
        jsonData = json.loads(response.text)

        for j in jsonData["list"]:
            n = n + 1
            # print(j["id"],j["source"],j["title"],j["addr"],j["pubDate"],j["info"])
            print('---------------------------------------------------------------------------')
            print(n, 'start!')
            policy_id = j["id"]
            addr = j["addr"]
            source = j["source"]
            title = j["title"]
            pubDate = j["pubDate"]
            print(addr, ' ', source)
            if not is_valid_date(pubDate[0:10]):
                continue
            today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if source in [u"科委", u"知识产权局"]:
                if compare_time(pubDate[0:10], recordTimeStr) <= 0:
                    continue
            else:
                if compare_time(pubDate[0:10], recordTimeStr) <= 0:
                    continue

            info = ''
            if "info" in j:
                info = j["info"]
            policy_data = {
                'policy_id': policy_id,
                'title': title,
                'addr': addr,
                'source': source,
                'pubDate': pubDate,
                'info': info
            }
            response = requests.post('http://47.95.10.33:8000/policy/addPolicy/', data=policy_data)
            print(response.text.encode("utf8"))


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


def scrap_policy():
    print('START')
    addrs = [
        u"中央",
        u"中央部委",
        u"北京市",
        u"天津市",
        u"河北省",
        u"东城区",
        u"西城区",
        u"朝阳区",
        u"海淀区",
        u"怀柔区",
        u"平谷区",
        u"丰台区",
        u"石景山区",
        u"顺义区",
        u"通州区",
        u"昌平区",
        u"大兴区",
        u"密云区",
        u"房山区",
        u"承德市",
        u"沧州市",
        u"邯郸市",
        u"衡水市",
        u"廊坊市",
        u"石家庄市"]
    # addrs = ["东城区","西城区","朝阳区","海淀区"]
    recordTime = requests.get('http://47.95.10.33:8000/policy/recordTime/')
    print('recordTime: ' + recordTime.text[0:10])
    recordTimeStr = recordTime.text[0:10]
    for addr in addrs:
        searchData(addr, recordTimeStr)
    print('END')


def test():
    with open('a.txt', 'w') as f:
        f.write('Hello, world!')
    print(6666)
    return 1


if __name__ == '__main__':
    scrap_policy()
