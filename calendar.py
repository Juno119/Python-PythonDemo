__author__ = 'YiTao'
# coding=utf-8

import time
import calendar
import datetime

#用ticks计时单位返回从12:00am, January 1, 1970(epoch) 开始的记录的当前操作系统时间
ticks = time.time()
print(ticks)

# 0	tm_year	2008
# 1	tm_mon	1 到 12
# 2	tm_mday	1 到 31
# 3	tm_hour	0 到 23
# 4	tm_min	0 到 59
# 5	tm_sec	0 到 61 (60或61 是闰秒)
# 6	tm_wday	0到6 (0是周一)
# 7	tm_yday	1 到 366(儒略历)
# 8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
localTime = time.localtime(time.time());
print(localTime);

#获取格式化的时间
localTime = time.asctime(time.localtime(time.time()));
print(localTime);

# print(time.timezone)
# cal = calendar.month(2014,8)
# print(cal)

print(datetime.date.today());
print(datetime.datetime.today());