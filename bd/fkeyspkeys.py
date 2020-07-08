import sqlite3

connection = sqlite3.connect("cursopython.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE (
      dni  VARCHAR(9) PRIMARY KEY,
      nombre  VARCHAR(100),
      edad  INTEGER,
      email  VARCHAR(100)
    )

''')

connection.commit()
connection.close()