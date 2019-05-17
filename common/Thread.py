# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/12/012

import threading
#线程池的装饰器
def thread_number(number):
    def my_thread(func):
        a = []
        for i in range(number):
            b = threading.Thread(target=func)
            a.append(b)
            b.start()
        for c in a:
            c.join()
        return func
    return my_thread