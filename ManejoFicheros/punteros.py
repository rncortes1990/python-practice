import io #stdio
archivo = open("arch.txt","r")
archivo.seek(5)#se situa en el caracter de una linea
lineas = archivo.read()

print (lineas)
import pickle
lista = [1,2,"hola",["holanda"]]
fichero = open("archivo.pckl","wb")
pickle.dump(lista,fichero)
fichero.close()
fichero = open("archivo.pckl","rb")
data = pickle.load(fichero)
print(data)