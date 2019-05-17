# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/18/018

import time
def my_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        tamp=func(*args,**kwargs)
        end_time=time.time()
        print("%s运行的时间是:%s"%(func.__name__,(end_time-start_time)))
        return tamp
    return wrapper