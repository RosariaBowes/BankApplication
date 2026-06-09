import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '#20Oakway2007',
    database = 'bank_application'
)

cursor = connection.cursor()

cursor.execute('SHOW TABLES')

tables = cursor.fetchall()
for table in tables:
    print(table[0])

cursor.close()
connection.close()