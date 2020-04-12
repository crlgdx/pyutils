<!--[toc]-->

# pyutils
```
日常使用的一些工具打包
```

## 安装和卸载
```shell script
pip install . 
or
pip install -e .
# 卸载
pip uninstall pyutils
```

## use
方法1
```shell
In [1]: import pyutils as pu

In [2]: pu.log_time()
1586608906.857981
2020-04-11 20:41:46

```
方法2
```
>> from pyutils import log_time
>> log_time()
1586608945.280929
2020-04-11 20:42:25
```
方法3
```
# 导入所有包
>> from pyutils import *
>> log_time()
1586608945.280929
2020-04-11 20:42:25
```
