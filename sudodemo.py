
import suds

__author__ = 'YiTao'


url = "http://www.thomas-bayer.com/axis2/services/BLZService?wsdl"
client = suds.client.Client(url)
print(client)


