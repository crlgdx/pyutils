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
from pyutils import loge

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


def request(url, post_data=None, header=None, method='get', timeout=10):
    """
    通用的网络请求 可自定义get 或者post
    :param url:
    :param post_data:
    :param header:
    :param method:
    :param timeout:
    :return:
    """
    if header is None:
        header = headers_common
    try:
        if method == 'post':
            if post_data is None:
                raise Exception('post_data is None')
            req = requests.post(url, data=post_data, headers=header, timeout=timeout)
            return req.text
        else:
            req = requests.get(url, headers=header, timeout=timeout)
            return req.text
    except Exception as e:
        loge(e)
        loge('请求错误')
        return 'nothing'
