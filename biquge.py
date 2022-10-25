#!/usr/bin/python
#coding:utf-8
# -*- coding:utf8 -*-
import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

nextp = ""

#http://m.biquge.info/40_40174/1515109.html
def pparser():
    basic_url = 'https://www.biq'

    bk1 = "/book/39798/";
    pn1 = "1050490";

    bk2 = "/book/41037/";
    pn2 = "1209490"
 
    bk3 = "/book/29250/"
    pn3 = "11559197"

    # 发起请求
    request_url = basic_url + "uge.com.cn" + bk3 + pn3 + ".html";
 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(request_url, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    htm = response.text
    # 解析内容
    soup = BeautifulSoup(htm, 'html.parser')
    # print(soup)



    print('------------------------------------------------------------------------------')
    # 标题
    title = soup.find(attrs={"name": "keywords"})
    print(title)
    

    print('------------------------------------------------------------------------------')
    # 正文
    # content = soup.find(attrs={"id": "content"})
    content = soup.find(id="content").contents
    for x in xrange(len(content)):
        if "<br" not in content[x].encode('utf-8'):
            print(content[x].encode('utf-8'))
            continue
        pass
    

    print('------------------------------------------------------------------------------')
    # 一章
    # nextp = soup.find_all('a')
    nparent = soup.find(attrs={"class": "bottem1"})
    print(nparent.contents[5])

if __name__ == '__main__':
    red_num = [] 
    blue_num = []
    # 调用函数
    pparser()


