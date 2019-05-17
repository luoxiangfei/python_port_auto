#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/10 17:13

import requests
import json
from common.MD5page import md5Page
from common.getYaml import get_yaml
from common.data_config import YAML_DIR
class K8sCardSend(object):
    '''发送短信接口'''
    def __init__(self):
        self.m = md5Page()
        self.yaml = get_yaml(YAML_DIR)
        self.data = '{"appId":"9b654e20983e4be0950ce66c6ab5aa64","callBackUrl":"http://card-consumer.meetyou1:22016/card-consumer",' \
                    '"cardDealerId":"063b7415e1424aa19217c822d0bf3be3","phone":"13694245189","uuid":"ae7285784f184b7ab7728121259c64b3"}'.replace(' ','')
        self.private_key="MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAm0l+1pR23kj7eB3xQOwef6nDbTPPiODLMsUEFnQXBF7DcT783yqq30TnAl49oNwAGNgg2F4NfyQB0qWC" \
                         "cz9nPwIDAQABAkAI/Ceqosx98BscyB69cuwQ1vHHz8eiU99uAJhL9EugpQNk452l6EWv6qaocDcHktUAWKCQW3mwmlFi5aJlEPgBAiEA+Pwzz3VRnmU3H7KUZj/kjFVc4qa" \
                         "H0Isvc88VrHmsuUECIQCfqX+qEfRZsjMj/2RXZJ8cDixURYwbu4QVORio9y+AfwIhANE1QOdxgXohO9cze0QLLaPI2jpLiVTujpm1iFWbC0nBAiBDnfoWIZJ1ZjWoWiG5rUC" \
                         "BFjOJ4QZMPGbcwhiCfmTcqwIhAK9SUrm/SIFIvm9GAtMpD79EWAEZsmy0S6/++e1FZew4"
    def __str__(self):
        pass
    def getSign(self):
        '''接口sign'''
        sign=md5Page().strRSA(self.private_key,self.data)
        return sign
    def send_card_port(self):
        "发送短信接口请求"
        header={"sign":self.getSign(),"Content - Type": "application/json",
        }
        data = json.loads(self.data)
        url=self.yaml["url"]["send_ccard"]
        response = requests.post(url, headers=header, json=data)
        print(response.text)
        return response.text
if __name__ == '__main__':
    t=K8sCardSend()
    t.send_card_port()
