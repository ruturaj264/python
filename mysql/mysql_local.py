import pymysql

connection = pymysql.connect(

    host='localhost',
    user='root',
    password='19A1a1k@rev0',
    database='ecom',
    port=3306

)

cursor = connection.cursor()

cursor.execute('SELECT * FROM customers limit 2')
rows = cursor.fetchall()
print(rows)