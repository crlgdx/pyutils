#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/4/11 3:25 下午    1.0         None
"""
__version__ = "0.1.2"

import time
import pickle
import re
import os
import random
import json
from .utils import loge, logd
from .pandas_util import (
    # pandas 常用操作
    pd2json, json2pd, pd2markdown
)
from .request_util import (
    # 网络请求
    request, post_request, get_request
)

from .rouge_score_dureader import get_dureader_sccore

def log_time():
    """
    打印当前系统时间
    """
    print(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def get_time():
    """
    获取当前时间戳
    """
    return time.time()


def get_time_with_year():
    """
    返回年月日
    :return:
    """
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def get_time_second():
    """
    返回13位时间戳
    @return:
    """
    t = time.time()
    time_second = int(round(t * 1000))
    return time_second


def print_time():
    print(time.time())


def mkdir(path):
    """
    创建路径
    @param path: 创建的路径
    @return: nothing
    """
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


def clean_str(row):
    """
    简单的清洗数据
    @param row: 输入字符串
    @return: 清洗后的字符串
    """
    row = re.sub('[\u3000\t]', ' ', row)
    row = re.sub('\s{2,}', '', row)
    row = re.sub('[“”]', '', row)
    row = re.sub('[\r\n]', ' ', row)

    row = re.sub(r'０', '0', row)
    row = re.sub(r'１', '1', row)
    row = re.sub(r'２', '2', row)
    row = re.sub(r'３', '3', row)
    row = re.sub(r'４', '4', row)
    row = re.sub(r'５', '5', row)
    row = re.sub(r'６', '6', row)
    row = re.sub(r'７', '7', row)
    row = re.sub(r'８', '8', row)
    row = re.sub(r'９', '9', row)
    row = re.sub(r'．', '.', row)
    return row


def is_file(str_file):
    """
    判断str是文件结尾or只是个文件夹， 默认认为文件是'.*'结尾，文件夹是'/*' or '\\' 结尾
    # 暂时废弃
    :param str_file:
    :return:
    """
    if '/' or '\\' in str_file.split('.')[-1]:
        # 是文件夹
        return False
    else:
        return True


def pickle_dump(obj_data, work_path='', file_name='obj_data.pkl'):
    """
    将 对象 数据存在本地，默认保存在当前位置 obj_data.pkl 命名
    @param obj_data: 源对象数据 任意对象
    @param work_path: 保存地址
    @param file_name: 保存文件名
    @:return 返回None
    """
    if '.pkl' in work_path:
        pickle.dump(obj_data, open(work_path, 'wb'))
        logd('save success:  ' + work_path + '\n')
        return None
    if work_path == '':
        pickle.dump(obj_data, open(os.path.join(work_path, file_name), 'wb'))
        logd('save success:  ' + file_name + '\n')
        return None
    mkdir(os.path.join(work_path))
    if '.' in file_name:
        pickle.dump(obj_data, open(os.path.join(work_path, file_name), 'wb'))
        file_name = os.path.join(work_path, file_name)
    else:
        pickle.dump(obj_data, open(os.path.join(work_path, file_name, '.pkl'), 'wb'))
        file_name = os.path.join(work_path, file_name)
    logd('save success:  ' + file_name + '\n')


def pickle_dump_simple(obj_data, save_file_path):
    """
    简单的pickl dump实现
    :param obj_data:
    :param save_file_path:
    :return:
    """
    pickle.dump(obj_data, open(save_file_path, 'wb'))
    print('save success:  ' + save_file_path + '\n')


def pickle_load(file_name_dir):
    """
    读取存在本地的数据 并返回, 传入地址与文件名
    @param file_name_dir: 保存地址
    @return: 源数据
    """
    obj_info = pickle.load(open(file_name_dir, 'rb'))
    return obj_info


def time_sleep_second(a=2, b=3):
    """
    睡眠 2-3 秒
    """
    time.sleep(random.randint(a, b))


def remove_duplicates_list(to_do_list):
    """
    对list去重，返回不重复的list，且顺序不变
    @param to_do_list:
    @return: 返回不重复的list
    """
    list2 = []
    for item in to_do_list:
        if item not in list2:
            list2.append(item)
    logd('去除重复{a}条'.format(a=(len(to_do_list) - len(list2))))
    return list2


def encode_key_word(str_data, encoding='utf-8'):
    """
    编码字符串为url格式
    @param str_data: 输入字符串
    @param encoding: 编码方式
    @return: 编码后的str
    """
    import urllib
    return urllib.parse.quote(str_data, encoding=encoding)


def decode_key_word(str_data, encoding='utf-8'):
    """
    解码码url数据 返回字符串
    @param str_data: 输入字符串
    @param encoding: 编码方式
    @return: 解码后的str
    """
    import urllib
    return urllib.parse.unquote(str_data, encoding=encoding)


def get_file_char(file_bytes):
    """
    输入bytes or bytearray, 返回属于某种字符集的概率
    :param file_bytes:
    :return:
    """
    import chardet
    fencoding = chardet.detect(file_bytes)
    return fencoding


def log_dict_key(dict_data: dict):
    """
    打印字典结构，key以及数据长度和类型
    :param dict_data:
    :return: None
    """
    for k in dict_data.keys():
        try:
            print('key: ', k, ' value_len: ', len(dict_data[k]), ' type: ', type(dict_data[k]))
        except Exception as e:
            print('key: ', k, ' value_len: ', ' type: ', type(dict_data[k]))


def json_save(json_data: dict, file_dir):
    """
    保存 json数据到本地
    :param json_data: 数据
    :param file_dir: 文件位置
    :return:
    """
    with open(file_dir, "w", encoding='utf-8') as dump_f:
        json.dump(json_data, dump_f, ensure_ascii=False, indent=4)


def json_save_list(json_data: dict, file_dir):
    """
    保存 list-json数据到本地,逐行保存
    :param json_data: 数据
    :param file_dir: 文件位置
    :return:
    """
    with open(file_dir, "w", encoding='utf-8') as writer:
        for item in json_data:
            writer.write(json.dumps(item, ensure_ascii=False) + "\n")


def json_dumps(json_data: dict, file_dir):
    """
    保存 json数据到本地
    :param json_data: 数据
    :param file_dir: 文件位置
    :return:
    """
    with open(file_dir, "w", encoding='utf-8') as writer:
        writer.write(json.dumps(json_data, indent=4, ensure_ascii=False) + "\n")


def json_read(file_dir, encoding='utf-8'):
    """
    读取本地json数据,默认utf-8格式打开
    :param file_dir:
    :return:
    """
    json_data = json.load(open(file_dir, encoding=encoding))
    return json_data


def read_josn_file_line(source_file_path):
    """
    逐行读取json file，并通过yield 返回json格式的数据
    :param source_file_path:
    :return:
    """
    with open(source_file_path, encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            yield data