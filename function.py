__author__ = 'YiTao'
# coding=utf-8

def printinfo(name,age=50):
    print(name)
    print(age)
    return ;
# printinfo("mike")
# printinfo("zhangshan",60)

def printinfo1(arg,*vartuple):
    print(arg)
    for var in  vartuple:
        print(var)
    return ;

# printinfo1(55)
#
# printinfo1(55,66,77)