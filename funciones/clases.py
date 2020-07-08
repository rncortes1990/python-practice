def retorno_tupla_multiple():
    return "hola",3,["a",2,"c"]

resultado=retorno_tupla_multiple()
string,number,lista=retorno_tupla_multiple()

print(resultado)
print(string,number,lista)
a,b,c=lista

print(a,b,c)
#para recorrer una lista con sus indices
# for idx,valor in enumerate(lista):º
l=[1,2,3] #lista
l[:] # copia de la lista

def funcion_indeterminada(*args):#tupla
    print(args)
def funcion_indeterminada_2(**args):#diccionario
    print(args)   
funcion_indeterminada(5,"hola",[1,2,3,4]) # retorna una tupla
funcion_indeterminada_2(a=5,c="hola",b=[1,2,3,4]) # retorna un diccionario

#funcion recursiva
def cuenta_atras(num):
    print("{}".format(num))
    num-=1
    if num>0:
        cuenta_atras(num)
    else:
        print("Booom!")
    print("Fin funcion {}".format(num))

cuenta_atras(5)