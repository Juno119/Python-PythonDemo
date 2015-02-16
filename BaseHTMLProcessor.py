#coding=utf-8
__author__ = 'YiTao'

from sgmllib import SGMLParser
import htmlentitydefs


class BaseHTMLProcessor(SGMLParser):
    def reset(self):
        self.pieces=[]
        SGMLParser.reset(self)