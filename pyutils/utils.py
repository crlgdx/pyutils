#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   utils.py    
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/4/12 10:05 下午    1.0         None
"""
import os


def logd(str_s):
    """
    打印 debug 信息
    @param str_s:
    @return:
    """
    print(str_s)


def loge(str_s):
    """
    打印 error 信息
    @param str_s:
    @return:
    """
    print('Error: ------------------- ')
    print(str_s)


def raise_alarm_mac(voice):
    """
    MaC 下调用系统命令行 输出警告语音
    :param voice: 输入文本
    :return: 输出语音
    """
    """
    Examples
    --------
    bash
    >>  say hello
    """
    os.system('say %s' % voice)


def raise_alarm_win(voice):
    """
    win平台下，调用系统发出警报
    :param voice:
    :return:
    """
    import winsound
    winsound.Beep(500, 1000)
