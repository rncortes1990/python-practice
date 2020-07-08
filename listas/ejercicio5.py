numeros=[1,3,6,9]

while True:

    n1=int(input("Ingresar numero a verificar"))
    if n1>=0 and n1<=9:
        break

if n1 in numeros:
    print("el numero", n1 ,"Existe en la lista")
else:
    print("el numero", n1 ,"No existe en la lista")
    