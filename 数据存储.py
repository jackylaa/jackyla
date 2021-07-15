import time
import traceback
import pymysql
import csv

def get_history():
    fn = csv.DictReader(open("C:/Users\小猪\PycharmProjects\Epidemic\历史数据.csv", encoding='utf-8'))
    #历史数据转化
    get_history = {}
    for row in fn:
        d = {}
        for k, v in row.items():
            get_history.setdefault(k, []).append(v)
    lable = ['comfirmed','comfirmed_add','suspect','suspect_add', 'crued','crued_add', 'died','died_add']
    for k, v in get_history.items():
        a=dict(zip(lable, v))
        get_history[k] = a
    return get_history
def get_details():
    fn1 = csv.reader(open("C:/Users\小猪\PycharmProjects\Epidemic\当日详细数据.csv", encoding='utf-8'))
    #详细数据转化
    get_details = []
    for row in fn1:
        get_details.append(row)
    get_details.pop(0)
    return get_details


def get_conn(conn, cursor):
    conn = pymysql.connect(  #创建链接
        host='localhost',
        user='root',
        password='root',
        db='疫情数据',
        charset='utf8'
    )
    cursor = conn.cursor()  #创建游标
    return conn, cursor

def close_conn(conn, cursor):   #关闭连接
    if cursor:
        cursor.close()
    if conn:
        conn.close()
#插入历史数据
def insert_history():
    conn = None
    cursor = None
    try:
        print(f"{time.asctime()}开始插入数据")
        conn, cursor = get_conn(conn, cursor)
        sql = 'insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for k,v in get_history.items():
            cursor.execute(sql, [k, v.get('comfirmed'), v.get('comfirmed_add'), v.get('suspect'), v.get('suspect_add'), v.get('crued'), v.get('crued_add'), v.get('died'), v.get('died_add')])
        conn.commit()
        print(f'{time.asctime()}插入数据完毕')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

def update_details():
    conn = None
    cursor = None
    try:
        li = get_details()
        conn, cursor = get_conn(conn, cursor)
        sql = "insert into details(update_time, province, city, comfirmed, comfirmed_add, crued, died) values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select update_time from details order by update_time desc limit 1)'
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新数据")
            for item in li:
                cursor.execute(sql,item)
            conn.commit()
            print(f"{time.asctime()}更新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)
def update_history():
    cursor = None
    conn = None
    try:
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn(conn, cursor)
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select comfirmed from history where dt=%s"

        for k, v in get_history().items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get('comfirmed'), v.get('comfirmed_add'), v.get('suspect'), v.get('suspect_add'), v.get('crued'),v.get('crued.add'), v.get('died'), v.get('died_add')])
                conn.commit()  # 提交事务 update delete insert操作
                print(f"{time.asctime()}历史数据更新完毕")
    except:
            traceback.print_exc()
    close_conn(conn, cursor)
get_history()
get_details()
update_history()
update_details()
