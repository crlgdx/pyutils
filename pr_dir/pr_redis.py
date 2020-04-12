#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   prredis.py
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/3/22 16:31    1.0         None
'''
import redis
import time

# 1、建立连接---python3.5的写法，不兼容
con = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=1,
    decode_responses=True  # 设置为True返回的数据格式就是时str类型
)

# 3、key的操作
res = con.keys('*')  # 查看所有的key
print(res)
# res = con.delete('Nmae')#删除key，返回删除的个数


con.set('string_key', 'string_value')
con.set('string_key_del', 'string_value')
print(con.get('string_key'))

# 添加数据
con.append('string_key', time.time())

# 删除数据
con.delete('string_key_del')

res = con.keys('*')  # 查看所有的key
print(res)

# 添加数据到列表
lista = [1, 2, 3, 4]
con.rpush('list_keys', 1)
con.rpush('list_keys', 3)
con.rpush('list_keys', 5)
con.rpush('list_keys', 7)
con.lpush('list_keys', '9')

# lrange---查看数据 起始位置
print(con.lrange('list_keys', 0, 11))

# lset---修改数据
# con.lset('list_F',1,'Fyn')---返回布尔值

# rpop ---- 随机删除一个数据
# con.rpop('keys')

# lrem ---- 指定删除一个数据时
# con.lrem('list_f',0,'okl')


# 1、字符串类型操作：
# set----键key
# con.set('key','values')
#
# get---获取数值
# con.get('com')
#
# append --- 追加
# con.append('keys','values')
#
# delete---删除
# con.delete('keys')

# 2、List类型：
#
# rpush 、lpush----添加数据
# con.rpush('keys','values')
# con.lpush('keys','values')
#
# lrange---查看数据
# con.lrange('list',0,11)
#
# lset---修改数据
# con.lset('list_F',1,'Fyn')---返回布尔值
#
# rpop ---- 随机删除一个数据
# con.rpop('keys')
#
# lrem ---- 指定删除一个数据时
# con.lrem('list_f',0,'okl')

# 3、Hash类型
#
# hmget --- 添加多条数据,也可插入单条数据
# 以字典的形式插入
# con.hmste('keys',{'name':''age})#插入结果返回布尔值

# hget , hgetall , hvals，hkeys查看数据
# con.hget('ok','name')
# con.hgetall('ok')#结果返回字典
# con.hvals('ok')#获取所有的键值
# con.hkeys('ok')#获取所有的键
#
# hdel 、 del----删除某个字段，删除整个hash
# con.hdel('ok',age)#指定删除某个字段 ，成功的话返回1，否则返回0
# con.del('ok')#删除整个hash

# 4、set
#
# sadd---添加数据
# con.sadd('mk','oi'.'Hwelo')
#
# smembers ---- 查看所有数据
# con.smembers('mk')
#
# spop---随机删除一个元素
# con.spop('con.spop('mk')')
#
# srem--- 指定删除某个元素
# con.srem('mk','oi')


# 5、sorted set
#
# zadd---添加数据
# con.zadd('set_f',{'name':1.1,'age':2,'sex':3})
#
# zrange ---- 查询数据
# con.zrange('set_f',0,11)
#
# zrem ---指定删除某个元素
# con.zrem('set_f','age')


# 6、redis-py管道操作 piplines
#
# 管道是redis的子类，它支持在一个请求中款冲多个命令到服务器
#
# #1、创建一个管道
# pipe = con.pipeline()
#
# #缓冲多个命令
# pipe.keys('*')
# pipe.set('name','Mkl')
# ​
# #执行命令
# res = pipe.execute()#返回列表
# print(res[0])
# print(res[1])
