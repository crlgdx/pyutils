#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   request_util.py    
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/4/12 9:57 上午    1.0         None
"""
import requests
import time
from .utils import loge, logd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

headers_common = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
                  "Safari/537.36 SE 2.X MetaSr 1.0",
}


def get_request(url, header=None, timeout=10):
    """
    通用的 get请求，传入url，可以自定义header
    @param url: 访问的url
    @param header: 访问头
    @param timeout: 超时设置
    @return: 如果成功，返回爬取的数据，否则返回 'nothing'
    """
    if header is None:
        header = headers_common
    try:
        req = requests.get(url, headers=header, timeout=timeout)
        return req.text
    except Exception as e:
        loge(e)
        loge('网络超时，正在暂停，10秒后继续爬取')
        time.sleep(10)
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            return req.text
        except Exception as e:
            loge(e)
            loge('网络超时，略过该次请求')
            # time.sleep(60)
            return 'nothing'


def post_request(url, post_data, header=None, timeout=10):
    """
    通用的 post请求,传入url，post_data,可以自定义header
    :param url:
    :param post_data:
    :param header:
    :param timeout: 超时设置
    :return: 如果成功，返回爬取的数据，否则返回 'nothing'
    """
    if header is None:
        header = headers_common
    try:
        req = requests.post(url, data=post_data, headers=header, timeout=timeout)
        return req.text
    except Exception as e:
        loge(e)
        loge('网络超时，正在暂停，10秒后继续爬取')
        time.sleep(10)
        try:
            req = requests.post(url, data=post_data, headers=header, timeout=timeout)
            return req.text
        except Exception as e:
            loge(e)
            loge('网络超时，略过该次请求')
            # time.sleep(60)
            return 'nothing'


def request(url, post_data=None, header=None, timeout=10):
    """
    通用的网络请求 可自定义get 或者post，post_data不为None时使用post请求，否则get
    :param url: 访问url
    :param post_data: 如果post方式，需有数据
    :param header: 请求头
    :param timeout: 超时时间
    :return: 请求错误时返回nothing
    """
    if 'http' not in url:
        logd('***  warning: may miss http or https in url: ' + url)
        url = 'https://' + url
    if header is None:
        header = headers_common
    try:
        if post_data is not None:
            req = requests.post(url, data=post_data, headers=header, timeout=timeout)
            return req.text
        else:
            req = requests.get(url, headers=header, timeout=timeout)
            return req.text
    except Exception as e:
        loge(e)
        loge('请求错误')
        return 'nothing'


def urllib_request(url, post_data=None, header=None, encoding="utf-8"):
    """
    通过系统自带请求库进行网络访问，如果pos_data不为None，通过post访问，否则get访问
    urlopen 后可接Request对象，或者直接为url地址
    :param post_data: 如果post方式，需有数据
    :param url: 访问url
    :param header: 请求头
    :param encoding: 默认解码方式，网页为gbk编码时，需要用户指定
    :return: 请求错误时返回nothing
    """
    if header is None:
        header = headers_common
    if post_data is None:
        # get 访问
        req = Request(url, headers=header)
    else:
        # post 访问
        req = Request(url, data=post_data, headers=header)
    try:
        response = urlopen(req)  # 请求
        html = response.read().decode(encoding=encoding)
        return html
    except Exception as e:
        loge(e)
        return 'nothing'


def bs4_find_class(html, class_value):
    """
    传入html文本或者网络数据流，返回匹配class标签的bs4.element.Tag list
    :param html: html文本或者未解码前的context
    :param class_value: class标签值
    :return: list
    """
    Soup = BeautifulSoup(html, 'lxml')
    soup_list = Soup.find_all(class_=class_value)
    return soup_list


def bs4_get_soup(html):
    """
    传入html文本或者网络数据流，返回BeautifulSoup对象
    :param html:
    :return:
    """
    Soup = BeautifulSoup(html, 'lxml')
    return Soup
