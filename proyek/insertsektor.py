import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='m26415031',
    passwd='tos',
    db='m26415031')
cursor = mydb.cursor()

csv_data = csv.reader(file('sectors.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO sektor(kode)VALUES(%s)', row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
