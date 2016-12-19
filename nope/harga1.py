#!/usr/bin/python

import json
import urllib2
import mysql.connector
import subprocess

db = mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor=db.cursor()

response = urllib2.urlopen('http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php')
data=response.read()

