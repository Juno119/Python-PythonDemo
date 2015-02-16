# encoding=utf-8
__author__ = 'YiTao'

import os
import sys
import logging
from datetime import *


class LogHelper:
    def __init__(self):
        self.log = self.getlog()

    def info(self, message):
        self.log.info(message)

    def error(self, message):
        self.log.error(message)

    def getlog(self):
        logger = logging.getLogger("LogHelper")
        formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S', )
        logpath = self.getcurrpath() + "/log"
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        file_handler = logging.FileHandler(logpath + "/%s.log" % date.today())
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def getcurrpath(self):
        #获取脚本路径
        path = sys.path[0]
        ##判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)