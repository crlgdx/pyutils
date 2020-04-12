import requests
import json
from pymongo import MongoClient
import urllib
import urllib.request
import time

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["spyderdb"]

db_list = ['gucci_test', 'gucci_test_1', 'gucci_test_2', 'gucci_test_3', 'gucci_test_4']

list_data = []
for db_name in db_list:
    mycol_gucci_test = mydb[db_name]

    all_data = mycol_gucci_test.find()
    for item in all_data:
        for _item in item['item']:
            list_data.append(_item)

print(len(list_data))

# l1 = ['b','c','d','b','c','a','a']
list_data_re = []
[list_data_re.append(i) for i in list_data if not i in list_data_re]

print(len(list_data))
print(len(list_data_re))
# print(len(a))

# 1
# 2149
# 2084


# 3
# 2313
# 2241

# all
# 7454
# 2970


# 121*20= 2420
