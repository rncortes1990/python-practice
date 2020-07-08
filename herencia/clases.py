class Producto:
    def __init__(self,
                referencia,
                nombre,
                pvp,
                descripcion):
        
        self.referencia=referencia
        self.nombre=nombre
        self.pvp=pvp
        self.descripcion=descripcion

    def __str__(self):
        return"""
Referencia ......\t{}
Nombre ..........\t{}
pvp .............\t{}
descripcion .....\t{}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion)
        
        
class Adorno(Producto):
        pass
        
class Alimento(Producto):
        productor = ""
        distribuidor = ""       
        def __str__(self):
            
            return"""
Referencia ......\t{}
Nombre ..........\t{}
pvp .............\t{}
descripcion .....\t{}
productor .......\t{}
distribuidor ....\t{}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
        isbn = ""
        autor = ""       
        def __str__(self):
            
            return"""
Referencia ......\t{}
Nombre ..........\t{}
pvp .............\t{}
descripcion .....\t{}
isbn ............\t{}
autor ...........\t{}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)



ad = Adorno("000A","cuadro pintado",15000,"cuando renacentista del siglo XVII")
al = Alimento("000A2","aceite oliva",7990,"aceite para ensaladas")
li = Libro("000B2","Don quijote",7990,"Las locas aventuras de un viejito demente")
li.isbn = "1400FHG"
li.autor = "Miguel De Cervantes"
al.productor = "belmont"
al.distribuidor = "walmart"

print(ad)
print(al)
print (li)

productos =[ad,al]

productos.append(li)
print(productos)

for producto in productos:
    print(producto)

import copy

al_copy= copy.copy(al)
al_copy.pvp=2000
print (al)
print (al_copy)