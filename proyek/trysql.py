#!/usr/bin/python

import mysql.connector

#open database connection
db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor=db.cursor()

sql="CREATE TABLE users (`user_id` BIGINT NULL AUTO_INCREMENT,`user_name` VARCHAR(45) NULL,`user_username` VARCHAR(45) NULL,`user_password` VARCHAR(45) NULL,PRIMARY KEY (`user_id`));";

try:
  cursor.execute(sql)
  db.commit()
except:
  db.text()
  db.rollback()

db.close()




