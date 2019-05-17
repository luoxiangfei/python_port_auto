#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/9 14:59
import json
from common.MD5page import md5Page
def test1():
    json1='{"appid":"e338fb6e73154efeafbf5f71e77611a0","phone":"13662460070","templateId":"5ca474c9ba20288cedef9031"}'
    str1=md5Page().strMD5("20190404095149")
    str2=md5Page().strMD5(json1)
    str3=md5Page().strMD5("{}RCS_SIGN{}".format(str1,str2))
    print(str3)
def test3():
    str1='9FE7E972B16A42B14EA3BB17332B1A5C'.lower()
    print(str1)
if __name__ == '__main__':
    test1()