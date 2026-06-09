import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password = '#20Oakway2007'
)

my_cursor = mydb.cursor()

my_cursor.execute('CREATE DATABASE bank_application')

my_cursor.execute('SHOW DATABASEs')
for db in my_cursor:
    print(db)
    