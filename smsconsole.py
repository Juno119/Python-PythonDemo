#encoding=utf-8
__author__ = 'YiTao'

import sys

argvLen = len(sys.argv)
if argvLen< 2:
    print("没有设置参数！！！")
    sys.exit()

print(sys.argv[1])

print(sys.argv[1].split(','))

for m in sys.argv[1].split(','):
    print(m)

print('' is None)
print('' is '')

