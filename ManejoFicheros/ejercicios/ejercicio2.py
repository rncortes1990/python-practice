# Ejercicio 2
# En este ejercicio deberás crear un script llamado contador.py que realice varias tareas sobre un fichero
# llamado contador.txt que almacenará un contador de visitas (será un número):

# Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o está vacío 
# lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
# Luego a partir de un argumento:
# Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
# Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
# Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
# Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
# Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.
from io import open
class Contador:
    def __init__(self):

        try:
            contador = self.__cargar_contador()
        except Exception as err:
            self.__contador="None"
            print ("Ocurrio un error: {}".format(err))
        else:
            self.__contador = contador
        
    def contador(self):
        if(type(self.__contador) is int):
            return self.__contador
        else:
            return "Contador no valido para el archivo"
    def increment(self):
        try:
            self.__contador+=1
        except Exception as err:
            print("Error: {}".format((err)))
        else:
            fichero = open("contador.txt","w")
            fichero.seek(0)
            fichero.write(str(self.__contador))
            fichero.close()
    def decrement(self):
        try:
            self.__contador-=1
        except Exception as err:
            print("Error: {}".format((err)))
        else:
            fichero = open("contador.txt","w")
            fichero.seek(0)
            fichero.write(str(self.__contador))
            fichero.close()
    def __cargar_contador(self):
            fichero = open("contador.txt","a+")
            fichero.seek(0)
            lineas = fichero.readlines()
            fichero.close()
            if len(lineas) == 0:
                fichero = open("contador.txt","a+")
                fichero.write("0")
                fichero.close()
            # elif len(lineas) == 1 and len(lineas[0])>1:
            #     raise Exception("se supera el maximo de digitos en la linea principal {}".format(len(lineas[0])))
            elif len(lineas)>1:
                raise Exception("se supera el maximo de lineas del fichero{}".format(len(lineas)))
            else:
                # SE LEE EL ARCHIVO
                fichero = open("contador.txt","r")
                a = fichero.readline()
                fichero.close()
                return int(a)

c = Contador()
print(c.contador())
c.increment()
c.decrement()