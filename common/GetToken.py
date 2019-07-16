# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/13/013

import requests
import json
from common.LogInfo import logger
def get_token(phone):
    for i in range(10):
        try:
            url = "http://192.168.203.151:13600/SC/v21/family/auth/token?mobile={}".format(phone)
            res = requests.get(url=url)
            res1 = json.loads(res.text)["body"]["data"]
            break
        except Exception as e:
            logger.error('token获取失败:%s'%phone)
            continue
    return res1
if __name__ == '__main__':
    a=get_token(13694245189)
    print(a)