#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/18 13:59

import requests
import json
import os
import urllib3
import time
from common.excel import Excel
from common.data_config import PROT_YAML_DIR,TEST_DATA_DIR
from common.MD5page import md5Page
from common.getYaml import get_yaml
class K8sCallLogSave(object):
    '''发送短信接口'''
    def __init__(self):
        self.m = md5Page()
        self.yaml = get_yaml(PROT_YAML_DIR)["call_log_save"]
    def get_sign(self,data):
        '''接口sign'''
        sign=self.m.strRSA(self.yaml["privateKey"],data)
        return sign
    def get_body(self,data):
        '''接口需要body参数（base64）'''
        body=self.m.strBase64(data)
        return body
    def call_log_dave_port(self,data):
        "通话日志保存接口请求"
        header={"sign":self.get_sign(data),"appId":self.yaml["appid"],"Content - Type": "application/x-www-form-urlencoded",
        }
        data = {"cipherText":self.get_body(data)}
        url=self.yaml["url"]
        response = requests.post(url=url, headers=header, data=data)
        res=json.loads(response.text)['msg']
        print(res)
        time.sleep(1.5)
        return res
    def run(self,excel_data):
        data_list=[]
        for data_test in excel_data:
            if int(data_test[0])==0:
                data_test.append("测试结果")
            else:
                dict_data = {"caller": data_test[1], "callTime": data_test[2], "region": data_test[3],
                             "time": data_test[4], "type": data_test[5]}
                if data_test[1] == '':
                    dict_data.pop("caller")
                elif data_test[2] == '':
                    dict_data.pop("callTime")
                elif data_test[3] == '':
                    dict_data.pop("region")
                elif data_test[4] == '':
                    dict_data.pop("time")
                elif data_test[5] == '':
                    dict_data.pop("type")
                result=self.call_log_dave_port(json.dumps(dict_data))
                data_test.append(result)
            data_list.append(data_test)
        return data_list
if __name__ == '__main__':
    data = '{"callTime":"2019-04-16 00:00:00","caller":"13694245189","region":"333","time":1,"type":"1"}'
    t=K8sCallLogSave()
    data1 = Excel().get_xls(r"{}/K8S_call_log_save_testdata/data.xlsx".format(TEST_DATA_DIR), "call_log_data")
    print(t.run(data1))
