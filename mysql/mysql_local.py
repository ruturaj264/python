import pymysql

ecom_conn = pymysql.connect(

    host='localhost',
    user='root',
    password='19A1a1k@rev0',
    database='ecom',
    port=3306

)

companyhr_conn = pymysql.connect(

    host='localhost',
    user='root',
    password='19A1a1k@rev0',
    database='companyhr',
    port=3306

)

ecom_cursor = ecom_conn.cursor()
companyhr_cursor = companyhr_conn.cursor()

ecom_cursor.execute('SELECT * FROM customers limit 2')
rows = ecom_cursor.fetchall()
print(rows)

companyhr_cursor.execute('SELECT * FROM departments limit 5')
rows = companyhr_cursor.fetchall()
print(rows)

ecom_cursor.close()
companyhr_cursor.close()
ecom_conn.close()
companyhr_conn.close()