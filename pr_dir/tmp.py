#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   tmp.py    
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/11/22 10:04    1.0         None
"""
import pyutils as pu

data = pu.read_tsv(r"D:\work\data_set\nlpcc-dbqa\dbqa_dev.tsv")

save_file = r"D:\work\data_set\nlpcc-dbqa\dbqa_dev.tsv"

for line in data:
    line[0],line[1],line[2],line[3] = line[1],line[2],line[3],line[0]

pu.save_tsv('./tmp.tsv', data)