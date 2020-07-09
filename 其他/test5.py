import pymysql

db = pymysql.connect(host='localhost',user='root',password='',db='spider',port=3306)
cursor = db.cursor()
data = {
    'id':'13151313',
    'name':'Bob',
    'age':20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table}({keys}) values ({values})'.format(table=table,key=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('ok')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()