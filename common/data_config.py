#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/26 11:08

import os
from common.getYaml import YamlReader


BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
PAGE_DIR = os.path.join(BASE_DIR, 'pagefile')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output_file')
YAML_DIR = os.path.join(PAGE_DIR,'page.yaml')
PROT_YAML_DIR = os.path.join(PAGE_DIR,'port_data.yaml')
TEST_DATA_DIR = os.path.join(PAGE_DIR,'test_data')

class Config:
    def __init__(self, config='page.yaml'):
        path = os.path.join(PAGE_DIR, config)
        self.config = YamlReader(path).data

    def get(self, element, index=0):
        return self.config[index].get(element)

if __name__ == '__main__':

    print(PROT_YAML_DIR)