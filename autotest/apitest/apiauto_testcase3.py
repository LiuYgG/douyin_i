# -*- coding: UTF-8 -*-
'''
@Project ：autotest 
@File    ：apiauto_testcase3.py
@Date    ：2021/8/8 18:44 
'''
import requests, time, sys, re
import urllib, zlib
import pymysql
import json
from trace import CoverageResults
from idlelib.rpc import request_queue
from time import sleep

HOSTNAME = '127.0.0.1'

# 读取数据空中相应的接口用例数据
def readSQLcase():
    # sql 语句
    sql = "SELECT id, `apiname`, `apiurl`, `apimethod`, `apiparamvalue`, `apiresult`, `apistatus` FROM apitest_apistep where" \
          "apitest_apistep.Apitest_id=3"
    # 打开 MySQL 数据库连接
    coon = pymysql.Connect(user='root', passwd='', db='autotest', port=3306, host=HOSTNAME, charset='utf8')
    # 读取数据库操作游标
    cursor = coon.cursor()
    # 执行 SQL 查询语句
    aa = cursor.execute(sql)
    # 获取执行查询语句后的结果数据列表
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        interfaceTest(case_list)
        # 提交
        coon.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        coon.close()