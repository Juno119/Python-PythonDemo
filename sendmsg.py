# encoding=utf-8
__author__ = 'YiTao'

import sys
import platform

from wsrequest import WsRequest
from loghelper import LogHelper


class MsgHelper:
    def __init__(self, mobiles, content, smsSource, supplierID, isVoiceSms):
        self.Mobiles = mobiles
        self.Content = content
        self.SmsSource = smsSource
        self.SupplierID = supplierID
        self.IsVoiceSms = isVoiceSms
        self.RequestXml = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Body>
                        <SendSmsSaveLog xmlns="http://tempuri.org/">
                          <mobile>%s</mobile>
                          <content>%s</content>
                          <smsSource>%s</smsSource>
                          <supplierID>%d</supplierID>
                          <isVoiceSms>%s</isVoiceSms>
                        </SendSmsSaveLog>
                      </soap:Body>
                    </soap:Envelope>"""


    def sendmessage(self):
        for m in self.Mobiles:
            self.sendsms(m, self.Content)

    def sendsms(self, mobile, content):
        if mobile is None or mobile is '':
            msg = "手机号为空！！！".decode('utf-8')
            LogHelper().info(msg)
            print(msg)
            return
        if content is None or content is '':
            msg = "短信内容为空！！！".decode('utf-8')
            LogHelper().info(msg)
            print(msg)
            return
        # print("手机号：%s\n短信内容：%s\n" % (mobile,content))
        SOAPMessage = self.RequestXml % (mobile, content, self.SmsSource, self.SupplierID, self.IsVoiceSms)
        # print(SOAPMessage)
        # print("\n")
        ws = WsRequest(SOAPMessage)
        result = ws.request()
        print(result)


if __name__ == "__main__":
    argvLen = len(sys.argv)
    if argvLen < 2:
        msg = "没有设置参数".decode('utf-8')
        # print(msg)
        LogHelper().info(msg)
        sys.exit()
    elif argvLen < 3:
        msg = "参数设置不全".decode('utf-8')
        print(msg)
        LogHelper().info(msg)
        sys.exit()
    else:
        print(sys.argv[1])
        print(sys.argv[2])
    mobiles = sys.argv[1].split(',')  # ['13269688234',]
    if cmp(platform.system(), 'Windows') == 0:
        content = sys.argv[2].decode('gbk').encode('utf-8')
    elif cmp(platform.system(), 'Linux') == 0:
        content = sys.argv[2]
    else:
        content = sys.argv[2]
    smsSource = "Python-短信通知"
    supplierID = 0
    isVoiceSms = 0
    msgHelper = MsgHelper(mobiles, content, smsSource, supplierID, isVoiceSms)
    msgHelper.sendmessage()


