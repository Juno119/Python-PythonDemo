# -*- coding: utf-8 -*-
import os
import sys


#-------遍历  d i c t i o n a r y------

print("===========方法一=============")
for k,v in os.environ.items():
    print("%s=%s" % (k,v))


print("===========方法二=============")
temp = "\n".join(["%s=%s" % (k,v) for k,v in os.environ.items()])
print(temp)


print("===========modules=============")
print("\n".join(sys.modules.keys()))


# sys.argv[0]表示代码本身文件路径
print(sys.argv[0])

#获取当前路径的方法
print(os.getcwd())

##=====获取脚本文件的当前路径==========
#获取脚本路径
path = sys.path[0]
##判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
if os.path.isdir(path):
    print(path)
elif os.path.isfile(path):
    print(os.path.dirname(path))

currentPath = os.getcwd()+"/log"
if not os.path.exists(currentPath):
    os.mkdir(currentPath)
print(currentPath)


print(sys.getdefaultencoding())
# print sys.argv[1]
# print(sys.argv[1].decode(sys.getdefaultencoding()).encode('utf-8'))

print (os.environ)

import platform
print(platform.mac_ver())
print(platform.version())
print(platform.system())

# print(cmp(platform.system(),'Windows'))