# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/28/028

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.data_config import PAGE_DIR,Config,OUTPUT_DIR

log_config = Config('log_config.yaml')

class Logger(object):
    '''日志打印的类'''
    def __init__(self, logger_name=log_config.get('logger_name')):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = log_config.get('log_file_name')
        self.backup_count = log_config.get('backup_count')
        # 日志输出级别
        self.console_output_level = log_config.get('console_output_level')
        self.file_output_level = log_config.get('file_output_level')
        # 日志输出格式
        self.formatter = logging.Formatter(log_config.get('formatter'))

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(
                filename=os.path.join(OUTPUT_DIR, self.log_file_name),
                when='D',
                interval=1,
                backupCount=self.backup_count,
                delay=True,
                encoding='utf-8'
            )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
if __name__ == '__main__':
    logger.info("sdf")

