# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/21/021
import yaml
import os
def get_yaml(url):
    '''读取yaml数据'''
    file=open(url,"r",encoding="utf-8")
    data=yaml.safe_load(file)
    return data
class YamlReader:
    '''读取YAML数据的类'''
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None
    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data
if __name__ == '__main__':
    t=YamlReader(r"..\pagefile\page.yaml").data
