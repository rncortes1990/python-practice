import sqlite3
import os
def connection():
    try:
        connection =  sqlite3.connect("restaurante.db")
    except Exception as err:
        raise Exception(err)
    else:
        return connection

def closedb(connection):
    try:
        connection.close()
    except Exception as err:
        raise Exception(err)
    else:
        print ("Base de datos cerrada")
        return True

def initdb(cursor):
    try:
        cursor.execute('''
            CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)
        ''')
        cursor.execute('''
            CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL, 
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except Exception as err:
        raise Exception(err)
    else:
        pass
def agregar_categoria(conn,nombre):
    try:
        cursor = conn.cursor()
        print(nombre)
        cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(nombre))
        conn.commit()
    except Exception as error:
        print("Error: {}".format(error))
    else:
        print ("categoria agregada!")
        pass
def initapp():
    
    conn = connection()
    # initdb(conn.cursor())
    while True:
        # os.system('clear')
        opcion = str(input('''
            Que desea realizar?:  \n
            [c]: Agregar categoria
        :_'''))
        if opcion.upper()=='C':
            # os.system('clear')
            print("=====Agregar categoria=====")
            categoria = str(input("Escriba nombre de categoria: "))
            agregar_categoria(conn,categoria)
        else:
            print("Debe elegir alguna de las opciones disponibles")    

    closedb(conn)

initapp()
