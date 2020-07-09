import pymysql

def get_cursor():
    conn = pymysql.connect(host='localhost',user='root',password='243043853',port=3306,db='bilibili')
    return conn

