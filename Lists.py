# coding=utf-8
__author__ = 'YiTao'

#列表(Lists)

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

print("list1[0]:%s" % list1[0])
print("list1[1:3]:%s " % list1[1:3])

#更新值
list1[3]="four"
print(list1)
#删除值
del list1[2]
print(list1)
#长度
print(len(list2))
#组合
print(list2+list3)
#重复
print(list2 * 2)
#元素是否存在于列表中
print("b" in list3)
#迭代
for x in list3:print(x);

print(list1[1])#读取列表中第2个元素
print(list1[-1])#读取列表中倒数第1个元素
print(list1[1:])#从第二个元素开始截取列表

#将元组转换为列表。
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple);
print(aList)

# temp = [123, 'xyz', 'zara', 'abc']
# print(temp.append('444'))

#任意无符号的对象，以逗号隔开，默认为元组
tup3 = "a", "b", "c", "d";
print(tup3)

print(range(7))
print(range.__doc__)
(MONDAY, TUESDAY , WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) =range(7)
print(MONDAY)
print(SUNDAY)