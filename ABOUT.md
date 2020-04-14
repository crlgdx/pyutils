# pyutils
```
日常使用的一些工具打包
```

## content

[__init__.py](pyutils/__init__.py)

[utils.py](pyutils/utils.py)

[pandas_util.py](pyutils/pandas_util.py)

[request_util.py](pyutils/request_util.py)

1、简单的处理工具

`utils.py` `__init__.py`

logd、loge


2、pandas常用工具

`pandas_util.py`

3、网络请求常用工具

`request_util.py`


## version 0.0.1
### 测试打包 安装和卸载
```shell script
# 将源文件拷贝到 *site-packages目录下
pip install . 
or
# 建立软连接，源码不会拷贝到python site-packages 目录下
pip install -e .
# 卸载
pip uninstall pyutils
```

```shell script

➜  ~ cd /Users/zcr/work/github_2020/pyutils 
➜  pyutils ls
pyutils  setup.py
# 安装
➜  pyutils pip install -e .
Obtaining file:///Users/zcr/work/github_2020/pyutils
Installing collected packages: pyutils
  Running setup.py develop for pyutils
Successfully installed pyutils
You are using pip version 9.0.1, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

# 卸载 
➜  pyutils pip uninstall pyutils
Uninstalling pyutils-0.0.0:
  /Users/zcr/anaconda3/lib/python3.6/site-packages/pyutils.egg-link
Proceed (y/n)? y
  Successfully uninstalled pyutils-0.0.0
You are using pip version 9.0.1, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
➜  pyutils 

```
## version 0.0.2
### 升级
若已存在低版本会卸载低版本后安装新版本
```shell script
➜  pyutils pip install .        
Processing /Users/zcr/work/github_2020/pyutils
Installing collected packages: pyutils
  Running setup.py install for pyutils ... done
Successfully installed pyutils-0.0.1
You are using pip version 9.0.1, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
➜  pyutils pip install .
Processing /Users/zcr/work/github_2020/pyutils
Installing collected packages: pyutils
  Found existing installation: pyutils 0.0.1
    Uninstalling pyutils-0.0.1:
      Successfully uninstalled pyutils-0.0.1
  Running setup.py install for pyutils ... done
Successfully installed pyutils-0.0.2
You are using pip version 9.0.1, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
➜  pyutils pip install .
Processing /Users/zcr/work/github_2020/pyutils
  Requirement already satisfied (use --upgrade to upgrade): pyutils==0.0.2 from file:///Users/zcr/work/github_2020/pyutils in /Users/zcr/anaconda3/lib/python3.6/site-packages
```
