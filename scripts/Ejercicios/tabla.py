# Crea un script llamado tabla.py que realice las siguientes tareas:

# Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
# En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# El script contendrá un bucle for que itere el número de veces del primer argumento.
# Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
# Ejecuta el código y observa el resultado.
# Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.


import sys

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])


if (num_1 and num_2) >= 1  and (num_1 and num_2) <= 9:
    print ("continua")
    for i in range(num_1):
        for i in range(num_2):
             print(" * ", end='')
        print()
else:
    print ("parametros incorrectos\n")
    print ("Ingrese dos numeros del 1 al 9\n")
    print ("ejemplo: python tabla.py 'x' 'y'\n")
