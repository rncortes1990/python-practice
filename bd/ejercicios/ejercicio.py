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
def agregar_plato(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categoria")
        categorias = cursor.fetchall()
        while True:
            print ("A que categoria añadirá un platillo")
            id_categorias = []
            for categoria in categorias:
                print ("[{}] {} \n".format(categoria[0],categoria[1]))
                id_categorias.append(categoria[0])
            print ("[{}] {} \n".format(9,"Salir"))
            opcion = int(input(">_ "))
            if opcion in id_categorias:
                nombre_plato = input("Ingrese nombre de platillo: \n")
                cursor.execute("INSERT INTO plato VALUES(null,'{plato}','{categoria}')".format(plato=nombre_plato,categoria=opcion))
                conn.commit()
                break
            elif opcion ==9:
                break
            else:
               print ("Opcion incorrecta")
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(nombre_plato))
    except Exception as error:
        print("Error: {}".format(type(error).__name__))
    else:
        print ("platillo agregado!")
        pass
def mostrar_menu(conn):
    try:
        conn.cursor().execute("SELECT * FROM plato ORDER BY categoria_id ASC")
        for plato in conn.cursor().fetchall():
            print ("{}".format(plato[1]))
    except Exception as err:
        print ("Error en ejecucion: {}".format (type(err).__name__))
    else:
        pass
def initapp():
    
    conn = connection()
    # initdb(conn.cursor())
    while True:
        # os.system('clear')
        opcion = str(input('''
            Que desea realizar?:  \n
            [1]: Agregar categoria \n
            [2]: Agregar plato \n
            [3]: Mostrar menú \n
            [9]: Salir
        :_'''))
        if opcion =='1':
            # os.system('clear')
            print("=====Agregar categoria=====")
            categoria = str(input("Escriba nombre de categoria: "))
            agregar_categoria(conn,categoria)
        if opcion == '2':
            agregar_plato(conn)
        if opcion == '3':
            mostrar_menu(conn)
        elif opcion=='9':
            os.system('clear')
            print("=====Salir=====")
            break
        else:
            print("Debe elegir alguna de las opciones disponibles")    

    closedb(conn)

initapp()