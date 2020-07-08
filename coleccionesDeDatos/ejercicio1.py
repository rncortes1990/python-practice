# listas son con brackets []
# tuplas son con parentesis ()
# conjuntos son con llaves {} se inicializan como set() 
# diccionarios se inicializa como var = {} son identicos a los objetos javascript
# filas
# pilas

usuarios = {"Marta", "David", "Elvira", "Juan","Marcos"}
administradores= {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")
print(list(administradores))

for usuario in usuarios:
    if(usuario in administradores):
        print(usuario,"- administrador")
    else:
        print(usuario,"- usuario")
