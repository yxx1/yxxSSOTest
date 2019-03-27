#coding:utf-8

import logging
import os
'''
config log file, output logs above -INFO- level
DEBUG INFO WARNING ERROR CRITICAL - low->high
'''


class Log:
    project_path = os.path.abspath(os.path.join(os.getcwd(), "."))
    logPath = project_path + "\\log\\huanxiTest.log"

    def __init__(self):
        self.logger = logging.getLogger("HuanxiTest")

    def set_message(self, level, msg):
        # 创建handler，用于写入日志文件
        fh = logging.FileHandler(self.logPath, 'a+')
        # 创建handler, 用于输出到控制台
        ch = logging.StreamHandler()
        # 设置日志格式，在里面自定义设置日期和时间
        formater = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s %(message)s ")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # add Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # add log information, output logs above -INFO- level
        self.logger.setLevel(logging.DEBUG)
        fh.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
        if level == 'debug':
            self.logger.debug(msg)
        elif level == 'info':
            self.logger.info(msg)
        elif level == 'warning':
            self.logger.warning(msg)
        elif level == 'error':
            self.logger.error(msg)
        # remove Handler, otherwise, log would repeat
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.set_message('debug', msg)

    def info(self, msg):
        self.set_message('info', msg)

    def warning(self, msg):
        self.set_message('warning', msg)

    def error(self, msg):
        self.set_message('error', msg)
