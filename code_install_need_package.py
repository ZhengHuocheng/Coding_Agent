#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import sys


# In[2]:


def install_needed_package(package_name: str,
                           python_executable=sys.executable):
    """
    传入包名，创建子进程进行安装,返回安装信息
    参数:
    package_name (str) -- 要安装的包的名称
    python_executable (str) -- 要使用的Python解释器的路径,默认使用当前Python环境
    """
    info = {}
    try:
        # check_output、call、check_all用法见：https://blog.csdn.net/liushuibufuqin/article/details/78892831
        output = subprocess.check_output([python_executable, "-m", 'pip', 'install', package_name],
                                         stderr = subprocess.STDOUT,
                                         shell = True)
        output = output.decode().strip("\n").strip()
        info["output"] = output
        return info["output"]
    except subprocess.CalledProcessError as e:
        info["output"] = {}
        info["output"]["returncode"] = e.returncode
        info["output"]["cmd"] = e.cmd
        info["output"]["output"] = e.output
        return info["output"]







