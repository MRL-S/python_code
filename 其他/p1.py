import pymysql
db = pymysql.connect(host='localhost',user='root',password='',db='spider',port=3306)
cursor = db.cursor()
data = {
    'id':'13151313',
    'name':'Bob',
    'age':22
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('ok')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()