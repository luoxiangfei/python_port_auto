#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/9 11:00

import requests
import json
import os
from common.excel import Excel
from common.MD5page import md5Page
from common.data_config import PROT_YAML_DIR,TEST_DATA_DIR
from common.getYaml import get_yaml
class K8s_send_sms(object):
    '''发送短信接口'''
    def __init__(self):
        self.m = md5Page()
        self.yaml = get_yaml(PROT_YAML_DIR)
        self.time = self.m.time_str()
        #self.time = "20190404095149"
        # self.data = '{"appid" : "e338fb6e73154efeafbf5f71e77611a0","phone" : "13694245189","templateId" : "5ca474c9ba20288cedef9031"}'.replace(' ','')
        #self.data = json.dumps({"appid":self.yaml["App-Id"],"phone":"13662460070","templateId":self.yaml["templateId"]})
    def __str__(self):
        pass
    def getSign(self,data):
        '''接口sign'''
        str1 = md5Page().strMD5(self.time)
        str2 = md5Page().strMD5(data)
        str3 = md5Page().strMD5("{}RCS_SIGN{}".format(str1, str2))
        return str3
    def send_sms_port(self,appid,phone,templateId):
        "发送短信接口请求"
        data='{"appid" : "%s","phone" : "%s","templateId" : "%s"}'.replace(' ','')%(appid,phone,templateId)
        header={"time":self.time,
            "sign":self.getSign(data),"Content - Type": "application/json",
        }
        data_new = json.loads(data)
        url=self.yaml["url"]["send_sms"]
        response = requests.post(url, headers=header, json=data_new)
        # res=json.loads(response.text)
        print(response.text)
        return response.text
    def run(self,excel_data):
        data_list=[]        #定义要一个空列表
        for data_test in excel_data:    #excel_data为测试数据，二维列表的形式
            if int(data_test[0])==0:        #先判断第一行第一列为0的时候，直接在这 一行的最后增加一个测试结果
                data_test.append("测试结果")
            else:
                result=self.send_sms_port(data_test[1],data_test[2],data_test[3])   #这里为进行接口请求，
                data_test.append(result)    #这里吧接口请求的结果写入到每行的最后一列
            data_list.append(data_test)   #这里把生成最新的每一列插入到列表data_list中
        return data_list                #这里吧生成的新二维列表返回出去
if __name__ == '__main__':
    t=K8s_send_sms()
    data_dir=os.path.join(TEST_DATA_DIR,'K8S_msg_card_testdata')
    data_excel_dir=os.path.join(data_dir,'send_msg_data.xlsx')
    data_excel = Excel().get_xls(data_excel_dir,'send_msg')
    result=t.run(data_excel)


