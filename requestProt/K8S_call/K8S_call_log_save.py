#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/18 13:59

import requests
import json
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
        data = {'cipherText':self.get_body(data)}
        url=self.yaml["url"]
        response = requests.post(url=url, headers=header, data=data)  #把请求头，请求参数，和url地址带进来接口请求，返回值给response
        res=json.loads(response.text)["msg"]    #把返回值转成字典格式然后取他的键'msg'，因为我这里知道了我需要的就是这个msg
        print(res)
        # time.sleep(4)
        return res                  #吧得到的数据返回出去
    def run(self,excel_data):
        data_list=[]        #定义要一个空列表
        for data_test in excel_data:    #excel_data为测试数据，二维列表的形式
            if int(data_test[0])==0:        #先判断第一行第一列为0的时候，直接在这 一行的最后增加一个测试结果
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
                result=self.call_log_dave_port(json.dumps(dict_data))   #这里为进行接口请求，
                data_test.append(result)    #这里吧接口请求的结果写入到每行的最后一列
            data_list.append(data_test)   #这里把生成最新的每一列插入到列表data_list中
        return data_list                #这里吧生成的新二维列表返回出去
if __name__ == '__main__':
    data = '{"callTime":"2019-04-16 00:00:00","caller":"13694245189","region":"333","time":1,"type":"1"}'
    t=K8sCallLogSave()
    data1 = Excel().get_xls(r"{}/K8S_call_log_save_testdata/data.xlsx".format(TEST_DATA_DIR), "call_log_data2")
    # for i in data1:
    #     print(i)
    t.run(data1)
