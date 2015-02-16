# encoding=utf-8
__author__ = 'YiTao'

import httplib
from xml.dom import minidom

from loghelper import LogHelper


class WsRequest:
    def __init__(self, soapmessage):
        self.RequestMethod = "POST"
        self.Host = "service.etaoshi.com"
        self.ContentType = "text/xml; charset=utf-8"
        self.SOAPAction = "http://tempuri.org/SendSmsSaveLog"
        self.Url = "service.etaoshi.com"
        self.MethodName = "/Sms.asmx"
        self.SoapMessage = soapmessage
        pass

    def request(self):
        """
        请求短信websevices
        :return:
        """
        log = LogHelper()
        try:
            webservice = httplib.HTTP(self.Url)
            webservice.putrequest("POST", self.MethodName)
            webservice.putheader("Host", self.Host)
            webservice.putheader("Content-type", self.ContentType)
            webservice.putheader("Content-length", "%d" % len(self.SoapMessage))
            webservice.putheader("SOAPAction", self.SOAPAction)
            webservice.endheaders()
            webservice.send(self.SoapMessage)

            print(self.SoapMessage)
            log.info(self.SoapMessage)
            statuscode, statusmessage, header = webservice.getreply()

            print ("Response: ", statuscode, statusmessage)
            # print "headers: "
            # print header
            res = webservice.getfile().read()
            log.info(res)
            print (res.decode('utf-8'))
            try:
                dom = minidom.parseString(res)
                nodes = dom.documentElement.getElementsByTagName('SendSmsSaveLogResult')
                if nodes is None or nodes[0] is None:
                    return "发送失败".decode('utf-8')
                else:
                    return nodes[0].firstChild.data
            except BaseException as ex:
                log.error("解析返回结果出错【%s】" % ex)
                print(ex)
                return "发送失败".decode('utf-8')
        except BaseException as ex:
            log.error("请求短信发送接口出错【%s】" % ex)
            print(ex)
            return "发送失败".decode('utf-8')

