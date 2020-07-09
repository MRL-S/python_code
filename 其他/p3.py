import pymysql

db = pymysql.connect(host='localhost',user='root',password='',db='spider',port=3306)
cursor = db.cursor()
sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    # print('count:',cursor.rowcount)
    # print("one:",cursor.fetchone())
    # print("results:",cursor.fetchall())
    result = cursor.fetchall()
    # print('results type:',type(cursor.fetchall()))
    for row in result:
        print(row)
except:
    print('error')