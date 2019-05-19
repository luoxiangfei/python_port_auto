#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/26 11:08

import os
from common.getYaml import YamlReader


BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]     #这个获取到框架根目录   E:\python_project\K8s_port_test
PAGE_DIR = os.path.join(BASE_DIR, 'pagefile')           #配置文件目录，就是根目录增加pagefile    E:\python_project\K8s_port_test\pagefile
OUTPUT_DIR = os.path.join(BASE_DIR, 'output_file')      #输出文件目录  E:\python_project\K8s_port_test\output_file
#下面都是路径
YAML_DIR = os.path.join(PAGE_DIR,'page.yaml')
PROT_YAML_DIR = os.path.join(PAGE_DIR,'port_data.yaml')
TEST_DATA_DIR = os.path.join(PAGE_DIR,'test_data')

class Config:
    '''读取yaml文件数据的类'''
    def __init__(self, config='page.yaml'):
        path = os.path.join(PAGE_DIR, config)
        self.config = YamlReader(path).data

    def get(self, element, index=0):
        '''获取yaml文件数据方法，类.get（数据名）'''
        return self.config[index].get(element)

if __name__ == '__main__':
    print(BASE_DIR)