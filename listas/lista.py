lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3=[]
for l1 in lista_1:
    if (l1 in lista_2) and (l1 not in lista_3):
        lista_3.append(l1)

print(list(lista_3))
