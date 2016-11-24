import sqlite3
# -*- coding: utf-8 -*-

db = sqlite3.connect('db1.db')
cursor = db.cursor()
#cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, password TEXT)''')
#db.commit()

#insert 
print('test inserts')
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
password1 = '12345'
name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

cursor.execute('''INSERT INTO users(id, name, phone, email, password) VALUES(NULL,'aaa','4234234','dfsdfs@aaaaa','aaaaaaa')''')
print('First user inserted')
cursor.execute('''INSERT INTO users(id, name, phone, email, password) VALUES(NULL,'bbb','5345346','fgdfgd@bbbb','bbbbbb')''')
print('Second user inserted')
db.commit()
#end of inserts

#fetching things
print('test fetching')
user1 = cursor.fetchone()
print(user1)

all_rows = cursor.fetchall()
for row in all_rows:
	print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
print('test all rows')

cursor.execute('''SELECT name, email, phone FROM users''')
for row in cursor:
	print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
print('test all rows')

user_id = 1
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user = cursor.fetchone()
#end of whatever it was

#test update
print('test update')
newphone = '3113093164'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ?''', (newphone, userid))
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
db.commit()
#end of this

db.close()
