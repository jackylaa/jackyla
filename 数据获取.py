import time

from 数据存储 import *

#获取历史数据函数
def get_data(sql):
    cursor, conn =None, None
    conn, cursor = get_conn(conn, cursor)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res[0]
#获取数据函数
def get_data1(sql):
    cursor, conn =None, None
    conn, cursor = get_conn(conn, cursor)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

def get_time():
    time_str = time.strftime("%Y{}%m{}%d %X")
    return time_str.format("年", "月", "日")
