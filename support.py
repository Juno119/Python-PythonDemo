__author__ = 'YiTao'
#coding=utf-8

import function

function.printinfo1(55,66,77)

#Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
from function import printinfo

printinfo("mike")


import math
#返回的列表容纳了在一个模块里定义的所有模块，变量和函数
content = dir(math)
print(content)

