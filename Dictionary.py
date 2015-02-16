# coding=utf-8
__author__ = 'YiTao'

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

#返回指定键的值，如果值不在字典中返回default值
print(dict.get("Alice"))
#返回 None
print(dict.get("dd"))

#如果键在字典dict里返回true，否则返回false
print(dict.has_key("Beth"))

#返回可遍历的(键, 值) 元组数组。
for yz in dict.items():
    print(yz)

#以列表返回一个字典所有的键
for k in dict.keys():
    print(k)
#以列表返回字典中的所有值
for v in dict.values():
    print(v)

for k,v in dict.items():
    print("%s=%s" % (k,v))
#循环遍历 dict 中的每个元素。对每个元素均执行如下操作：首先临时将其值
#赋给变量 k,v，然后 Python 应用函数 "%s=%s" % (k,v) 进行计算，最后将计算结果
#追加到要返回的 list 中。
print(["%s=%s" % (k,v) for k,v in dict.items()])
