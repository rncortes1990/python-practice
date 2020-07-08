import sys
print("script con entradas")
print(sys.argv)

# root@7e4c254ee680:/home/python/scripts# python entradas.py hola mundo
# script con entradas
# ['entradas.py', 'hola', 'mundo']

# texto= sys.argv[1]
# repeticiones = sys.argv[2]
texto= "hola"
repeticiones = 3
for n in range(int(repeticiones)) :
    print(texto)

n = "Raúl"
p = "Ingenieria civil en informática"

v = "soy {} y estudie {}".format(n,p)
print (v)
v = "soy {1} y estudie {0}".format(n,p)
print (v)
v = "soy {nombre} y estudie {profesion}".format(nombre=n,profesion=p)
print (v)

print("delimitacion de textos")
print ("{:>30}".format("palabra"))#30 espacios a la derecha
print ("{:30}".format("palabra"))#30 espacios a la izquierda
print ("{:^30}".format("palabra"))#al centro de 30 espacios en total
print ("{:.5}".format(p))#cantidad de letras
print ("{:>30.5}".format(p))#cantidad de letras y espaciadas
print("Formateo de  numeros")
print ("{:4d}".format(10))
print ("{:4d}".format(100))
print ("{:4d}".format(1000))
print("Formateo de  numeros con ceros")
print ("{:04d}".format(10))
print ("{:04d}".format(100))
print ("{:04d}".format(1000))
print("Formateo de  flotantes")
print ("{:.3f}".format(3.1415926))
print ("{:.3f}".format(153.21))
print ("{:7.3f}".format(3.1415926))
print ("{:7.3f}".format(153.21)) #son 7 flotantes por el punto del decimal
print ("{:07.3f}".format(3.1415926))
print ("{:07.3f}".format(153.21))
