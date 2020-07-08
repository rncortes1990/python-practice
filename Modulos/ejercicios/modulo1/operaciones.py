# Ejercicio 1
# Crea el siguiente módulo:

# El módulo se denominará operaciones.py y contendrá 4 funciones 
# para realizar una suma, una resta, un producto y una division entres dos números. 
# Todas ellas devolverán el resultado.
# En las funciones del módulo deberá de haber tratamiento e invocación manual de errores 
# para evitar que se quede bloqueada una funcionalidad, eso incluye:
# TypeError: En caso de que se envíen valores a las funciones que no sean números. 
# Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
# ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer 
# un mensaje que informe Error: No es posible dividir entre cero.
import logging

def suma(x,y):
    try:
        isNumber(x)
        isNumber(y)
    except TypeError:
        print ("Error de TIPO: valor no numerico")
    else:
        print("numeros validos")
        return sum([x,y])

def resta(x,y):
    try:
        isNumber(x)
        isNumber(y)
    except TypeError as err:
        print ("Error de TIPO: valor no numerico {}".format(err))
    else:
        return x-y
def producto(x,y):
    try:
        isNumber(x)
        isNumber(y)
    except TypeError:
        print ("Error de TIPO: valor no numerico")
    # except Exception as e:
    #     print(type(e).__name__)
    else:
        return x*y

def division(x,y):
    try:
        isNumber(x)
        isNumber(y)
        division = x/y
    except TypeError:
        print ("Error de TIPO: valor no numerico")
    except ZeroDivisionError:
        print ("No puede dividirse por {}".format(y))
    else:
        return division
def isNumber(number):
        if(type(number)is int or type(number)is float):
            logging.info('valor numerico')
        else:
          raise TypeError(number)
