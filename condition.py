#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'YiTao'

print(__author__)

flag = False
name = 'mike'
if name == 'mike':
    flag = True
    print('welcome')
else:
    print(name)

num = 9
if num > 0 and num < 10:
     print('ok')
else:
     print('no')

tag = 1
while tag<=10:
    print(tag)
    tag+=1
else:
    print(tag)

for letter in "python":
    print(letter)

fruits = ['apple','orange','banana']
for fruit in  fruits:
    print(fruit)
###序列索引迭代
for index in range(len(fruits)):
    print(fruits[index])

age = ("23","24","25")
for a in age:
    print(a)

###嵌套循环输出2~100之间的素数
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1

###pass是空语句，是为了保持程序结构的完整性。
for letter in 'Python':
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

##随机数
import  random
# 0-1之间的数
print(random.random())
#---choice() 方法返回一个列表，元组或字符串的随机项
print(random.choice([1,2,3,4,5,6]))
print(random.choice("I am student"))
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
print(random.choice(tuple))

#random.randrange ([start,] stop [,step])
#start -- 指定范围内的开始值，包含在范围内。
#stop -- 指定范围内的结束值，不包含在范围内。
#step -- 指定递增基数。基数缺省值为1。
print(random.randrange(100,1000,2))
print(random.randrange(100,1000))

print(random.seed(10))

#uniform() 方法将随机生成下一个实数，它在[x,y]范围内。
print(random.uniform(5,10))


import math
print(math.pi)
print(math.e)