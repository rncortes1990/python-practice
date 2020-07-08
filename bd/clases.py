import sqlite3

connection = sqlite3.connect("cursopython.db")
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100),edad INTEGER,email VARCHAR(199))")
except Exception as err:
    print("Error: {}".format(err))

# cursor.execute("INSERT INTO usuarios VALUES('RAUL CORTES',29,'cortesrau@gmail.com')")
# cursor.execute("SELECT * from usuarios")
# usuario = cursor.fetchone()
# print("{}".format(usuario))
# usuarios = [
#     ('JOSE BELEN V', 29, 'jbsanhueza@gmail.com'),
#     ('LUIS ORTIZ M', 25, 'lortizt@gmail.com'),
#     ('PHIL DUBO  L', 33, 'pdubolau@gmail.com')
# ]
# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)",usuarios)
cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR (9) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    edad INTEGER NOT NULL,
    email VARCHAR(199)NOT NULL
    )
""")
cursor.execute("UPATE usuarios SET nombre='raulozio' WHERE dni='1231A')"
cursor.execute("DELETE  FROM usuarios WHERE dni='1231A')"
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
print(usuarios)
connection.commit()

connection.close()