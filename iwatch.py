#!/usr/bin/python
#coding:utf-8
# -*- coding:utf8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from collections import Counter
import schedule
import time
#获取当前路径
import os
import imageio 
import matplotlib.pyplot as plt
fig=plt.figure()
f1 = fig.add_subplot(121)
isbuy = True

def httpGetRequest():
    print('------------------------------------------------------------------------------');
    ala = [];
    try:
        request_url = 'https://www.apple.com.cn/shop/refurbished/watch/apple-watch-series-7';
        #request_url = 'https://google.com';
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.get(request_url, headers=headers, timeout=5)
        response.encoding = 'utf-8'
        htm = response.text
        soup = BeautifulSoup(htm, 'html.parser')
        #print(soup);
        #print('------------------------------------------------------------------------------')
        nparent = soup.find("div", attrs={"class": "rf-refurb-category-grid-no-js"})
        #print(nparent);
        #print('------------------------------------------------------111-------')
        ala = nparent.find_all('a');
    except Exception:
        print('http请求超时');
        print(ala);
    date_str = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())
    print(date_str)
    for one in ala:
        name = str(one.contents)
        print(name)
        if "Apple Watch Nike Series 7 (GPS + 蜂窝网络)；45" in name:
        #if "Apple Watch Series 7 (GPS + 蜂窝网络)；41" in name:
            print(name)
            spect = imageio.imread('/Users/chengrongzhong/Desktop/颢颢嘟嘴.jpeg') 
            f1.imshow(spect)
            plt.show()
            isbuy = False
            continue
        pass
    # div = soup.find_all('div', {'class':'rf-refurb-category-grid-no-js'})
    # print(div);
    # print('---------------------------------------------------------------------------')

if __name__ == '__main__':
    # 调用函数 
    # httpGetRequest();
    schedule.every(15).seconds.do(httpGetRequest)
    while isbuy:
        schedule.run_pending()
    time.sleep(1)


