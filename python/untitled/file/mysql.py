
#encoding=utf-8
import sys
import pymysql
import uuid

#PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

db = pymysql.connect("localhost","root","88888888","university")
cursor = db.cursor()

name = 'sdfsdf1'
score =62

sql = ["SELECT * FROM SCORE",
       "INSERT INTO SCORE VALUES ( '%s', %s )" %(name,score)]
score_id = str(uuid.uuid1())
print(score_id)
print(type(score_id))
school='No 2'
position= 'henan'
type='理科'
batch='第一批次'
year='2016'
lowscore = '525'
avrscore = '600'
sql2 = "INSERT INTO SCORE VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (score_id,school, position, type, batch, year, lowscore, avrscore)

try:
    print(sql2)
    cursor.execute(sql2)
    cursor.execute(sql[0])
    result = cursor.fetchall()
    print(result)
    db.commit()
except:
    print("Error")


db.close()