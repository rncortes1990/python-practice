import math
import random
def leerNumero(ini,fin,mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            pass
        else:
            if valor >= ini and valor <= fin:
                break
    return valor

def generador():
    numeros= leerNumero(1,20,"Cuantos numeros desea generar? [1-20]")
    modo = leerNumero(1,3,""" modo de redondeo?
    [1] superior, [2] inferior, [3] normal
    """)
    lista_nums = []
    for num in range(numeros):
        # Generar random
        numero = random.uniform(0,101)
        print (numero)
        if modo == 1:
            print ("El num a la superior es: {}".format(math.ceil(numero)))
            lista_nums.append(math.ceil(numero))
        elif modo == 2:
            print ("El num a la inferior es: {}".format(math.floor(numero)))
            lista_nums.append(math.floor(numero))
        elif modo == 3:
            print ("El num a la normal es: {}".format(round(numero)))
            lista_nums.append(round(numero))
    return lista_nums            

generador()
