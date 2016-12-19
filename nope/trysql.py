#!/usr/bin/python

import mysql.connector

#open database connection
db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor=db.cursor()

sql="CREATE TABLE users (`userid` BIGINT NULL AUTO_INCREMENT,`username` VARCHAR(45) NULL,`actualname` VARCHAR(45) NULL,`email` VARCHAR(45) NULL,`password` VARCHAR(45) NULL,PRIMARY KEY (`userid`));";

try:
  cursor.execute(sql)
  db.commit()
except:
  db.text()
  db.rollback()

db.close()




