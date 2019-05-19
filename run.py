# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/24/024
#
import os
# from pip._internal import main as install_requirements
# install_requirements(['install', '-r', 'requirements.txt'])
from common.excel import Excel
from common.getYaml import get_yaml
from common.LogInfo import logger
from common.osCommand import DelDate
from common.send_email import SendEmail
from common.timeDecorator import my_time
from common.data_config import YAML_DIR,PAGE_DIR,OUTPUT_DIR,TEST_DATA_DIR
from requestProt.K8S_call.K8S_call_log_save import K8sCallLogSave
import time

class PortAutoTest(object):
    def __init__(self):
        '''获取数据配置'''
        self.data=get_yaml(YAML_DIR)
        self.excel = self.data["excel"]
        self.email = self.data["email"]
        self.time=time.strftime("%Y%m%d-%H%M%S")
        self.excel_name=self.time+self.excel["name"]
        self.report_new = os.path.join(OUTPUT_DIR,'report')
        self.report_excel = os.path.join(self.report_new,self.excel_name)
        self.log=logger
    @my_time
    def run_test(self):
        data = Excel().get_xls(r"{}/K8S_call_log_save_testdata/data.xlsx".format(TEST_DATA_DIR), "call_log_data")
        result_data=K8sCallLogSave().run(data)
        # 获取到接口返回信息
        Excel().write_newxls(result_data,self.report_excel,sheet="call_log_data2")
        #生成测试报告文件--excel
        time.sleep(2)
        connectEmail=SendEmail(self.email["addresser"],self.email["addressee"],self.email["smtp"],self.email["user"],self.email["passwd"])
        #连接邮箱
        connectEmail.email_init(self.report_excel,self.excel_name)
        #把测试报告发送到指定邮箱
        DelDate().del_run(num=3)
        #删除本地excel文件
        self.log.info ("----程序结束----")
if __name__ == '__main__':
    p=PortAutoTest()
    p.run_test()
