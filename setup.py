#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   setup.py
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/4/11 3:36 下午    1.0         None
"""
from setuptools import setup
from pyutils import __version__
# packages 要写完全，包括所有依赖的文件夹，否则安装时会失败
setup(
    name='pyutils',
    description='My python utils',
    url='https://gitee.com/lduml/pyutils',
    author='lduml',
    author_email='cr_lgdx@163.com',
    license='MIT',
    packages=['pyutils', 'pyutils.rouge_bleu_metric'],
    version=__version__,
    python_requires=">=3.5.0",
    zip_safe=False
)
