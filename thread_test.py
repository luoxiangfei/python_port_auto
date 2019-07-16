#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/19 17:55
import random
# from pip._internal import main as install_requirements
# install_requirements(['install', '-r', 'requirements.txt'])
from requestProt.K8S_call.K8S_call_log_save import K8sCallLogSave
from common.timeDecorator import my_time
import threading   #多线程模块


a=(i for i in range(1,100000000))
def port_fun():
    phone = random.randint(10000000, 99999999)
    data = '{"caller":"136%s","callTime":"2019-04-16 00:00:00","region":"020","time":1,"type":"1"}' % phone
    try:
        result=K8sCallLogSave().call_log_dave_port(data)
        print(result+"次数为%s"%next(a))
    except Exception as e:
        print("连接失败")

def run(bingfa):
    '''并发测试--多线程'''
    a=[]
    for i in range(int(bingfa)):                    #设置并发数量
        b=threading.Thread(target=port_fun)
        a.append(b)
        b.start()
    for c in a:
        c.join()
@my_time
def run_num(bingfa,xunhuan):
    '''测试循环次数'''
    for i in range(int(xunhuan)):                      #设置循环次数
        run(bingfa)
if __name__ == '__main__':
    bingfa=1000
    xunhuan=1000
    run_num(bingfa,xunhuan)
    CGL = (next(a) - 1) / (bingfa * xunhuan)
    print("成功为【{}】次，执行请求【{}】次，成功率为【{}】".format((next(a) - 2), (bingfa * xunhuan), str(CGL * 100) + '%'))