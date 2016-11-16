#!/usr/bin/python

import mysql.connector

#open database connection
db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor=db.cursor()

sql="INSERT INTO songs VALUES (NULL,'What','What'),(NULL,'Yes','No'),(NULL,'Now','Then')";

try:
  cursor.execute(sql)
  db.commit()
except:
  db.text()
  db.rollback()

db.close()

