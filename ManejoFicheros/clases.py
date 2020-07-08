import io #stdio

texto ="texto de linea1\nTexto de linea2\nTexto de linea3"
archivo = open("arch.txt","w")
archivo.write(texto)
archivo.close()

archivo = open("arch.txt","r")
lineas  = archivo.readlines()
archivo.close()
print(lineas)
print(lineas[2])
fichero = open("arch.txt","a")
fichero.write("\nTexto desde app")
fichero.close()
with open("arch.txt","r") as fichero:
    for linea in fichero:
        print(r"{}".format(linea))