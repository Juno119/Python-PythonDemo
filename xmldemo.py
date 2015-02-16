#encoding=utf-8
__author__ = 'YiTao'

from xml.dom import minidom

xmltemp = """<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>"""

dom = minidom.parseString(xmltemp)
root = dom.documentElement
bb = root.getElementsByTagName('maxid')
b= bb[0]
print b.firstChild.data


ll = root.getElementsByTagName('login')
l= ll[0]
print l.nodeName
print l.getAttribute("username")


xmltemp1="""<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>"""

dom1 = minidom.parseString(xmltemp1)
root1 = dom1.documentElement
# bb1 = root1.getElementsByTagName('SendSmsSaveLogResult')
# print(bb)