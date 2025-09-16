import mysql.connector

conn = mysql.connector.connect(

    host = 'bank-rds.cz6aacak4fmf.ap-south-1.rds.amazonaws.com',
    user = 'bank_rds_admin',
    password = '19A1a1krev0',
    database = 'bankdb',
    port=3306

)

cursor = conn.cursor()

# CREATE table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

# INSERT one row
cursor.execute("INSERT INTO users (name, age) VALUES (%s,%s)", ("Alice",30))
conn.commit()
print("Inserted ID:", cursor.lastrowid)

# INSERT multiple rows
cursor.executemany("INSERT INTO users (name, age) VALUES (%s,%s)", [("Bob",25),("Charlie",28)])
conn.commit()
print("Rows inserted:", cursor.rowcount)

# UPDATE
cursor.execute("UPDATE users SET age=%s WHERE name=%s", (31, "Alice"))
conn.commit()
print("Rows updated:", cursor.rowcount)

# DELETE
cursor.execute("DELETE FROM users WHERE name=%s", ("Bob",))
conn.commit()
print("Rows deleted:", cursor.rowcount)

# SELECT
cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
print("All users:", all_rows)

# Fetch one
cursor.execute("SELECT * FROM users WHERE name=%s", ("Alice",))
row = cursor.fetchone()
print("Single user:", row)

# Fetch many
cursor.execute("SELECT * FROM users")
rows = cursor.fetchmany(2)
print("Fetch many:", rows)

# Cursor attributes
print("Row count:", cursor.rowcount)
print("Description:", cursor.description)

# Stored procedure example
# cursor.callproc('my_proc', (param1,param2))
# for result in cursor.stored_results(): print(result.fetchall())

# Close cursor and connection
cursor.close()
conn.close()