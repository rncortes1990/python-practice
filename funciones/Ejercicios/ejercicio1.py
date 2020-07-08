# Realiza una función llamada area_rectangulo(base, altura) que 
# devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura:
def area_rectangulo(base, altura):
     return (base*altura)

A=area_rectangulo(15,10)
print(A)

# Realiza una función llamada area_circulo(radio) 
# que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio:
import math
print(math.pi)

def area_circulo(radio):
    return (math.pi*(radio**2))

AR=area_circulo(5)
print(AR)

# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5

def relacion(a, b):
    if(a>b):
        return 1
    elif(a<b):
        return -1
    else:
        return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

# Realiza una función llamada intermedio(a, b) 
# que a partir de dos números, devuelva su punto intermedio. 
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

def intermedio(a, b):
    return (a+b)/2

print (intermedio(-12, 24))

# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el 
# límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero>maximo:
        return maximo
    else:
        return numero

print(recortar(15,0,10))

# Ejercicio 6
# Realiza una función separar(lista) que tome una lista de números 
# enteros y devuelva dos listas ordenadas. La primera con los números pares y
#  la segunda con los números impares.

def separar(lista):
    pares=[]
    impares=[]
    for el in lista:
        if el%2==0:
            pares.append(el)
        else:
            impares.append(el)
    return sorted(pares),sorted(impares)
pares, impares = separar([-12, 84, 13, 20, -33, 101, 9])
print(pares)
print(impares)