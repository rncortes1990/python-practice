#creando excepciones
try:
    n = float(input("introduzca un numero"))
    m = 4
    print("{}/{} = {}".format(n,4,n/m))
except:
    raise Exception ("error de input")