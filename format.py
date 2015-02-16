#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'YiTao'


# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址

print("My name is %s,age is %d" % ("mike",32))

#把字符串的第一个字符大写
print("hello world".capitalize())

#返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(" Hello ".center(12,'m'))
#count() 方法用于统计字符串里某个字符出现的次数
print("Hello".count('l',0,3))
print("Hello".count('l'))

#find() 方法检测字符串中是否包含子字符串 str
str1 = "this is string example....wow!!!"
str2 = "exam"
print(str1.find(str2))
print(str1.find(str2,40))

#转换 string 中的小写字母为大写
print(str1.upper())
#翻转 string 中的大小写
print(str1.swapcase())
#返回"标题化"的 string,就是说所有单词都是以大写开始
print(str1.title())
#如果 string 是标题化的(见 title())则返回 True，否则返回 False
print(str1.istitle())
#如果 string 中只包含空格，则返回 True，否则返回 False.
print(str1.isspace())
print(" ".isspace())