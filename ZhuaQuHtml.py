__author__ = 'YiTao'
# encoding=utf-8


#@description:baidutiba content



import sys
import re
import httplib
import urllib


from sgmllib import SGMLParser


class BaidutiebaParser(SGMLParser):
    '''在百度贴吧里采集相应的关键字的标题'''


    def reset(self):


        SGMLParser.reset(self)

        self.info = []  #

        self.q_check = 0

        self.num = 0

        self.strcontent = ''


    def start_td(self, tag):


        '''匹配 标签'''

        if len(tag) != 0 and tag[0][1] == 's':
            self.num = self.num + 1

            self.q_check = 1


    def handle_data(self, text):


        '''处理文本'''

        txt = text.strip()

        if txt and self.q_check:


            for i in checklist:


                pipei = r'%s' % str(i)  #在要匹配的信息里找到和关键字匹配

                check_pan = re.compile(pipei)

                if check_pan.search(txt) is not None:


                    self.info.append(txt)


                else:


                    continue

        self.strcontent = '$|$'.join(self.info)


    def end_td(self):


        '''匹配'''

        self.q_check = 0


############################################配置信息#############################


keylist = ['我的贴身']  #贴吧名称

checklist = ['张家界', '韩国']  #要查询的关键字

content = {}  #采集内容

for m in keylist:


    page = 0

    keyword = urllib.quote(m.decode('utf-8').encode('gbk'))

    for i in xrange(10):
        # http://tieba.baidu.com/f/index/forumpark?pcn=%D0%A1%CB%B5&pci=161&ct=0&rn=20&pn=1
        url = '''http://tieba.baidu.com/f/index/forumpark?pcn=%s&pci=161&ct=0&rn=20&pn=%s''' % (
        str(keyword), str(page))

        data = urllib.urlopen(url).read()

        data = unicode(data, 'gbk').encode('utf-8')

        parser = BaidutiebaParser()

        parser.feed(data)

        content[i + 1] = parser.strcontent

        page = page + 50

for k in content.keys():
    print k

    print content[k]


