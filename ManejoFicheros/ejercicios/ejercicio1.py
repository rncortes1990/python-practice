# Ejercicio 1
# En este ejercicio deberás crear un script llamado personas.py
# que lea los datos de un fichero de texto, que transforme cada fila
# en un diccionario y lo añada a una lista llamada personas. Luego recorre las personas 
# de la lista y paracada una muestra de forma amigable todos sus campos.
# El fichero de texto se denominará personas.txt y tendrá el siguiente contenido 
# en texto plano (créalo previamente):
# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006

from  io import *
from pickle import *

def carga_de_datos():
    fichero = open("personas.txt","r",encoding="utf8")
    lineas = fichero.readlines()
    personas = []
    for linea in lineas:
        persona=linea.replace("\n", "").split(";")
        personas.append({"id":persona[0],"nombre":persona[1],"apellido":persona[2],"nacimiento":persona[3]})
    fichero.close()
    return personas
def print_listado(lista):
    for persona in lista:
        print("||{}|{}|{}|{}||".format(persona["id"],persona["nombre"],persona["apellido"],persona["nacimiento"]))


a = carga_de_datos()
print (a)

print_listado(a)