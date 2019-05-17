# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/27/027

import os
import shutil
from common.LogInfo import logger
from common.data_config import OUTPUT_DIR

def os_remove(filename):
    if os.path.exists (filename):
        os.remove (filename)
        logger.info(filename+"删除成功")
    else:
        logger.error("失败，{}文件不存在".format(filename))

def os_download(command):
    os.system(command)

def os_path():
    path1=os.path.split (os.path.dirname (os.path.abspath (__file__)))[0]
    return path1


class DelDate:
    '''删除框架报告文件'''
    def del_dir(self,file_path,num):
        '''删除文件夹操作'''

        try:
            while True:
                dir = os.listdir(file_path)
                dir.sort(key=lambda fn: os.path.getmtime(file_path + '\\' + fn))
                if len(dir)>int(num):
                    filepath = os.path.join(file_path, dir[0])
                    shutil.rmtree(filepath)
                    logger.info("删除成功，文件目录：{}".format(filepath))
                    continue
                else:
                    break
        except Exception as  e:
            logger.error('删除文件失败{}'.format(e))
    def del_file(self,file_path,num):
        '''删除文件操作'''

        try:
            while True:
                dir = os.listdir(file_path)
                dir.sort(key=lambda fn: os.path.getmtime(file_path + '\\' + fn))
                if len(dir)>int(num):
                    filepath = os.path.join(file_path, dir[0])
                    os.remove(filepath)
                    logger.info("删除成功，文件目录：{}".format(filepath))
                    continue
                else:
                    break
        except Exception as  e:
            logger.error('删除文件失败{}'.format(e))
    def del_run(self,num=5):
        '''删除旧的生成文件'''
        dir =  os.path.join(OUTPUT_DIR,'report')
        self.del_file(dir,num)
if __name__ == '__main__':
    d=DelDate()
    d.del_run()
