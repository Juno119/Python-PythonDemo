__author__ = 'YiTao'
# coding=utf-8

import io

# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

file = open("C:\Users\YiTao\Desktop\Canvas.txt", "r")

print(file.name)
print(file.closed)
print(file.mode)
print(file.read())
file.seek(0, 0)
print("------")
print(file.readline())
print(file.readline())
#如果文件没有关闭，关闭文件
if not file.closed:
    file.close()

print("=====================")

fo = open("C:\Users\YiTao\Desktop\Canvas.txt", "r+")

#读取的字节计数
print(fo.read(10))
#当前位置
print(fo.tell())
#把指针再次重新定位到文件开头
print(fo.seek(0, 0))
print(fo.read(10))
if not fo.closed:
    fo.close()

print("==============异常处理===================")

try:
    fo = open("C:\Users\YiTao\Desktop\Canvas.txt","r+")
    try:
        fo.seek(-128,2)
        print(fo.read(128))
    finally:
        if not fo.closed:
            print("关闭文件")
            fo.close()
except IOError:
    print("异常")
    pass

print("==============目录操作===================")
import os

#在当前目录下创建新的目录
try:
    os.mkdir("newdir");
except:
    print("目录已经存在");
    # print(ex.message);
else:
    print("创建目成功")
#改变当前的目录
os.chdir("newdir")
#方法显示当前的工作目录
print(os.getcwd())

#改变当前的目录,返回上一级目录
os.chdir("..")
print(os.getcwd())
#删除目录
os.rmdir("newdir")





