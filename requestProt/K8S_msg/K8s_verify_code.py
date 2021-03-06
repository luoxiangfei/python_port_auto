#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/9 17:17

import requests
import json
from common.MD5page import md5Page
from common.data_config import PROT_YAML_DIR
from common.getYaml import get_yaml
class K8s_verify_code(object):
    '''发送短信接口'''
    def __init__(self):
        self.m = md5Page()
        self.yaml = get_yaml(PROT_YAML_DIR)
        self.time = self.m.time_str()
        #self.time = "20190404095149"
        self.data = '{"appid":"e338fb6e73154efeafbf5f71e77611a0","code":"161620","phone":"13694245189"}'.replace(' ','')
        #self.data = json.dumps({"appid":self.yaml["App-Id"],"phone":"13662460070","templateId":self.yaml["templateId"]})
    def __str__(self):
        pass
    def getSign(self):
        '''接口sign'''
        str1 = md5Page().strMD5(self.time)
        str2 = md5Page().strMD5(self.data)
        str3 = md5Page().strMD5("{}RCS_SIGN{}".format(str1, str2))
        return str3
    def verify_code_port(self):
        "发送短信接口请求"
        header={"time":self.time,
            "sign":self.getSign(),"Content - Type": "application/json",
        }
        data = json.loads(self.data)
        url=self.yaml["url"]["verify_code"]
        response = requests.post(url, headers=header, json=data)
        # res=json.loads(response.text)
        print(response.text)
        return response.text
if __name__ == '__main__':
    t=K8s_verify_code()
    t.verify_code_port()



