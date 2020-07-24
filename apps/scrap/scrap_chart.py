# _*_ coding: utf-8 _*_
import os
import sys

# reload(sys)
sys.setdefaultencoding('utf-8')

# print sys.getdefaultencoding()

# 通过在发送post请求时添加一个data参数，这个data参数可以通过字典构造成
import requests
import json
import time


def searchData(tab, tab2, title, paramField):
    url = "http://www.tech110.net/template/cis_season/portal/portal_tj.php?paramField=" + paramField

    response = requests.get(url)
    jsonData = response.text
    jsonData = str(jsonData).replace('u\'', '\'').decode("unicode-escape")
    # print jsonData.encode("utf8")
    chart_data = {
        "tab": tab,
        "tab2": tab2,
        "title": title,
        "data": jsonData
    }
    response = requests.post('http://47.94.160.142:8001/policy/addChart/', data=chart_data)
    print(response.text.encode("utf8"))


def printData(tab, tab2, title, paramField):
    print(sys.getdefaultencoding())
    print(tab.encode("utf8"), tab2.encode("utf8"), title.encode("utf8"), paramField.encode("utf8"))


def scrap_chart():
    # print sys.getdefaultencoding()
    print('START')
    clues = [
        [u"科技成果库分析", u"成果类型", u"科技成果成果类型分布", u"1.1"],
        [u"科技成果库分析", u"地域分布", u"科技成果地域分布", u"1.6"],
        [
            u"科技成果库分析", u"年份分布", u"科技成果年份分布",
            u"1.2"],
        [
            u"科技成果库分析", u"应用行业", u"科技成果应用行业分布", u"1.5"],
        [u"科技成果库分析", u"学科分布", u"科技成果学科分布", u"1.3"],
        [
            u"科技成果库分析", u"工程与技术", u"工程与技术学科的子类分布",
            u"1.4"],
        [
            u"科研机构分析", u"按单位类型统计", u"科研机构单位类型统计", u"2.1"],
        [u"科研机构分析", u"按所在省份统计", u"各省份拥有的科研机构数量统计", u"2.2"],
        [u"科研机构分析", u"按行业分布统计", u"科研机构行业分布统计", u"2.3"],
        [u"科研人才分析", u"年份统计", u"2010-2014年科技成果完成人员总数", u"4.4"],
        [u"科研人才分析", u"年龄结构", u"科研人才年龄结构统计", u"4.1"],
        [
            u"科研人才分析", u"学历构成", u"科研人才学历构成统计", u"4.2"],
        [
            u"科研人才分析", u"职称构成", u"科研人才职称构成统计", u"4.3"],
        [
            u"应用技术成果分析", u"课题来源", u"应用技术成果课题来源分布", u"3.1"],
        [u"应用技术成果分析", u"评价方式", u"应用技术成果评价方式分布", u"3.2"],
        [u"应用技术成果分析", u"水平分布", u"应用技术成果水平分布", u"3.3"],
        [u"应用技术成果分析", u"所处阶段", u"应用技术成果所处阶段分布", u"3.4"],
        [u"应用技术成果分析", u"高新技术领域", u"应用技术成果高新技术领域分布", u"3.6"],
        [u"应用技术成果分析", u"体现形式", u"应用技术成果体现形式分布", u"3.5"],
        [u"应用技术成果分析", u"知识产权", u"科技成果类型分布", u"3.7"],
        [
            u"应用技术成果分析", u"应用情况", u"应用技术成果应用情况分布",
            u"3.8"],
        [u"可转化成果分析", u"年份", u"可转化成果年份分布", u"5.1"],
        [u"可转化成果分析", u"地域", u"可转化成果地域分布", u"5.5"],
        [
            u"可转化成果分析", u"完成单位", u"可转化成果完成单位类型分布", u"5.6"],
        [u"可转化成果分析", u"高新技术领域", u"可转化成果高新技术领域分布",
         u"5.4"],
        [u"可转化成果分析", u"学科", u"可转化成果学科分布", u"5.2"]
    ]
    for tab, tab2, title, paramField in clues:
        searchData(tab, tab2, title, paramField)
        # printData(tab, tab2, title, paramField)
    print('END')


if __name__ == '__main__':
    scrap_chart()
