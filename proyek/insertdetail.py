import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='m26415031',
    passwd='tos',
    db='m26415031')
cursor = mydb.cursor()

csv_data = csv.reader(file('data.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO detail(id,kode_emiten,perubahan,tanggal)VALUES(%s,%s,%s,%s)',row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"

