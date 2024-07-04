#!/usr/bin/env python
# coding: utf-8

# In[2]:


import io
import contextlib
from time import perf_counter as timer


# In[6]:


def excute_python_code(code: str):
    """
    运行Python代码块，返回运行结果
    """
    str_buffer = io.StringIO()  # 字符串缓冲区
    run_success = True          # 标识代码运行状态
    vars = locals()             # 返回关于当前局部变量的字典
    
    start_time = timer()
    
    with contextlib.redirect_stdout(str_buffer):
        try:
            # 代码执行
            exec(code,vars)
        except Exception as e:
            run_success = False
            print(f"[INFO]: Code Running Wrong | {str(e)}")
            
    end_time = timer()
    
    # 在缓冲区接受代码运行结果
    sys_output = str_buffer.getvalue()
    
    # 关闭缓冲区
    str_buffer.close()
    time_taking = end_time - start_time
    # 返回运行结果
    info = f"Code Run Successfully,Taking {time_taking:.5f} Seconds.\nCode Output: {sys_output}" if run_success else f"Failing Run Code,Taking {time_taking:.5f} Seconds.\nCode Output: {sys_output}"
    return info


# # In[9]:


# code = """print("I'm your creator")"""
# info = excute_python_code(code)


# # In[10]:


# print(info)


# # In[ ]:




