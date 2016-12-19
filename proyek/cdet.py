#!/usr/bin/python
import mysql.connector
db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")
cursor=db.cursor()
#sql = "CREATE TABLE sektor (`kode` VARCHAR(50) NOT NULL,PRIMARY KEY (`kode`));";
#sql = "CREATE TABLE emiten (`kode` VARCHAR(50) NOT NULL,`kode_sektor` VARCHAR(50) NOT NULL,PRIMARY KEY (`kode`), FOREIGN KEY (`kode_sektor`) REFERENCES sektor(`kode`) ON DELETE CASCADE);";
sql = "CREATE TABLE detail (`id` VARCHAR(5) NOT NULL ,`kode_emiten` VARCHAR(50) NOT NULL,`perubahan` DECIMAL(4,2) NOT NULL,`tanggal` DATE NOT NULL,PRIMARY KEY (`id`), FOREIGN KEY (`kode_emiten`) REFERENCES emiten(`kode`) ON DELETE CASCADE);";
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()
db.close()

