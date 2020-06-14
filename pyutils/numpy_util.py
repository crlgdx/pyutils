#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   numpy_util.py    
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/6/15 0:08    1.0         None
"""
import numpy as np


def softmax(x):
    """
    输入 array x，返回softmax数组
    >>>m = np.random.randn(2,  2)
    >>>softmax(m)
    -----------------------------------
    array([[-3.28619825, -1.12572678],
           [-0.73000486, -0.30344964]])

    array([[0.10335675, 0.89664325],
           [0.39494921, 0.60505079]])

    :param x:
    :return:
    """
    x_row_max = x.max(axis=-1)
    x_row_max = x_row_max.reshape(list(x.shape)[:-1] + [1])
    x = x - x_row_max
    x_exp = np.exp(x)
    x_exp_row_sum = x_exp.sum(axis=-1).reshape(list(x.shape)[:-1] + [1])
    softmax = x_exp / x_exp_row_sum
    return softmax

