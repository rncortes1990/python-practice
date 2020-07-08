# Ejercicio 1
# Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento 
#-respondió otro monje#ni las banderolas ni el viento, 
#lo que se mueve son vuestras mentes -dijo el maestro

string="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
lineas = string.split("#")
for idx,linea in enumerate(lineas):
    lineaCap=linea.capitalize()
    if idx == 0:
        
        lineas[idx]=lineaCap +"....."
        print(lineas[idx])
    else:
        lineas[idx]="- "+lineaCap
        print(lineas[idx])

# Ejercicio 2
# Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo,
#  concuerda con el primer número de la lista, tal que así:


def listTransform(lista):
    ltuple = list(set(lista))
    ltuple.sort(reverse=True)
    laux=[]
    suma=0
    for element in ltuple:
        if(element%2==0):
            laux.append(element)
            suma+=element
    laux.insert(0,suma)
    return laux

def stringizer(lista):
    return "".join(str(el) for el in lista)

def modificarLista(lista=[]):
    if(isinstance(lista,list)):
        verificator = stringizer(lista)
        if(verificator.isdigit()):
            return listTransform(lista)
        else:
            print("lista no numerica")           
    else:
        print("No es una lista!")

lista=modificarLista([1,1,2,2,5,7,8,9,9,10])
print("------------\n\n\n")
print(lista[0]==sum(lista[1:]))
modificarLista([2,2,"a",7,9,1])
modificarLista()
modificarLista(2)

# print([1,1,2,2,5,7,9,9,1].sort())