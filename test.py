#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'YiTao'

import sys

s="Hello world"
print(s)
print(s[0:5])
print(s[0])
print(s[1:])
print(s*2)

###Python列表
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (tinylist * 2)
print (list + tinylist)

###Python元组
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (tinylist * 2)
print (list + tinylist)

###Python元字典
dict = {}
dict["one"]="This is one"
dict[2]="This is two"

tinydict = {'name':'john','code':9726,'age':33}

print(dict["one"])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())