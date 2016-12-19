#!/usr/bin/python
import mysql.connector
db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")
cursor=db.cursor()
sql="LOAD DATA INFILE 'sectors.csv' INTO TABLE sektor FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';"
#sql="LOAD DATA INFILE 'emitents.csv' INTO TABLE emiten FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';"
#sql="LOAD DATA INFILE 'data.csv' INTO TABLE detail FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';"
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()
db.close()

