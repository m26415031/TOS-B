import mysql.connector

db = mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor = db.cursor()

file = open('/home/TOS-B/proyek', 'r')
file_content = file.read()
file.close()

query = "INSERT INTO company VALUES (%s)"

cursor.execute(query, (file_content,))

db.commit()
db.close()
