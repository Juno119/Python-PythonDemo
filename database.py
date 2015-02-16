#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# -------------------------------------------------------------------------------
# Name:        导出数据库数据.py
# Purpose:
#
# Author:      
#
# Created:     
#-------------------------------------------------------------------------------


import os
import pymssql
import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")


class MSSQLHelper():
    """docstring for MSSQLHelper"""

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(as_dict=True, host=self.host, user=self.user, password=self.pwd, database=self.db,
                                    charset="utf8")
        # as_dict=True,可以通过列名访问
        # cur=self.conn.cursor(as_dict=True)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        resList = cur.fetchall()
        #查询完毕后关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        self.conn.commit()
        self.conn.close()

    def Query(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        row = cur.fetchone()
        while row:
            print ("%s %s" % (row['title'], row['context']))
            row = cur.fetchone()
            pass
        self.conn.close()

    def Query1(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        for row in cur:
            print ('row = %r' % (row,))
            print ('title=%s, context=%s' % (row['title'], row['context']))
            pass
        self.conn.close()


def main():
    db = "tempdb"
    user = "sa"
    password = "tiger"
    host = 'USER-20150213WU'
    sql = "select name from sysobjects where xtype='U'"
    sql1 = "SELECT * FROM sys.objects AS o WHERE o.[type]='s'"
    ms = MSSQLHelper(host=host, user=user, pwd=password, db=db)
    for (name,) in ms.ExecQuery(sql):
        print(name)
    print ('---------fetchall()---------')
    for item in ms.ExecQuery(sql1):
        for r in item:
            print (r)
        print (item)
        # print ('%s %s' % (item['title'], item['context']))
    print ('---------fetchone()---------')
    # ms.Query(sql1)

    print ('---------for row in cur---------')
    # ms.Query1(sql1)


if __name__ == '__main__':
    main()
    print("OK") 

 

