# Crea un script llamado descomposicion.py que realice las siguientes tareas:

# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:ç
import sys

if(len(sys.argv)==2):
    num = sys.argv[1]
    if(int(num)>=1):
        numberLenght = 0
        n=str(len(num))
        for i in num[::-1]:
            suma = (int(i)*(10**(numberLenght)))
            numberLenght+=1
            print("{suma:0{total_digitos}d}".format(suma=int(suma),total_digitos=n))
    else:
        print("Parametros incorrectos\n El script se debe ejecutar como: 'python descomposicion.py x'")
else:
    print("Parametros insuficientes")