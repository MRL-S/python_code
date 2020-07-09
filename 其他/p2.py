import pymysql

db = pymysql.connect(host='localhost',user='root',password='',db='spider',port=3306)
cursor = db.cursor()
table = 'students'
condition = 'age > 20'
sql = 'delete from {table} where {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()