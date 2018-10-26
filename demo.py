# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.selector import Selector
import time
import os


def writeFile(dirPath, page):
    data = Selector(text=page).xpath("//td[@class='zwmc']/div/a")
    titles = data.xpath('string(.)').extract()
    timeMarks = Selector(text=browser.page_source).xpath("//td[@class='gxsj']/span/text()").extract()
    links = Selector(text=browser.page_source).xpath("//td[@class='zwmc']/div/a/@href").extract()

    for i in range(len(titles)):
        fileName = titles[i].replace(':', '-').replace('/', '-').replace('\\', '-').replace('*', 'x').replace('|',
                                                                                                              '-').replace(
            '?', '-').replace('<', '-').replace('>', '-').replace('"', '-').replace('\n', '-').replace('\t', '-')
        filePath = dirPath + os.sep + fileName + '.txt'

        with open(filePath, 'w') as fp:
            fp.write(titles[i])
            fp.write('$***$')
            fp.write(timeMarks[i])
            fp.write('$***$')
            fp.write(links[i])


def searchFunction(browser, url, dirPath):
    browser.get(url)

    # 去除广告
    browser.find_element_by_xpath("/html/body/ins[@id='LXB_CONTAINER']/ins[@class='lxb-hide-btn']").click()
    browser.find_element_by_xpath("/html/body/div[@id='LRdiv2']/div[@id='LRfloater2']/div[@id='LRMINIWIN']/div[@id='LRMINIWIN0']/span[2]/img/@src").click()


    # 定位搜索框
    browser.find_element_by_xpath("/html/body/div[@class='wrap clear ']/div[@class='policyLeft']/h3/div[@class='filter']/b[@class='thisSite checkads']/i[@class='check1']").click()

    # 确认搜索
    browser.find_element_by_xpath("/html/body/div[@class='wrap clear ']/div[@class='policyLeft']/h3/div[@class='filter']/div[@class='addressWrap clear']/p[@class='showCheck1 showCheck hover']/i[@class='check0']").click()

    totalCount = Selector(text=browser.page_source).xpath("//span[@class='search_yx_tj']/em/text()").extract()[0]
    pageOver = int(totalCount) / 40
    for i in range(pageOver):
        time.sleep(3)
        writeFile(dirPath, browser.page_source)
        browser.find_element_by_link_text("下一页").click()

    time.sleep(3)
    writeFile(dirPath, browser.page_source)


if __name__ == '__main__':
    print 'START'
    url = 'http://www.jszyfw.com/grabNoti/'
    dirPath = u"policyData"

    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    # 定义一个火狐浏览器对象
    browser = webdriver.Chrome()
    searchFunction(browser, url, dirPath)

    browser.close()
    print 'END'