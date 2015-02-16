# encoding=utf-8
__author__ = 'YiTao'

import HTMLParser


class TitleParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.taglevels = []
        self.handledtags = ['title', 'body']  # 提出标签
        self.processing = None
        HTMLParser.HTMLParser.__init__(self)
    #开始标签
    def handle_starttag(self, tag, attrs):
        if tag in self.handledtags:
            self.data = ''
            self.processing = tag
    #标签内容
    def handle_data(self, data):
        if self.processing:
            self.data += data
    #结束标签
    def handle_endtag(self, tag):
        if tag == self.processing:
            print str(tag) + ':' + str(tp.gettitle())
            self.processing = None

    def gettitle(self):
        return self.data

fd=open('test.html','r')
tp=TitleParser()
tp.feed(fd.read())