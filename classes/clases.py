class Galleta():
    chocolate = False
    def __init__(self,sabor="bocado",color="cafe claro"):
        self.sabor=sabor
        self.color=color
        print("Se ha creado una galleta {1} sabor {0} ".format(self.sabor,self.color))
    def chocolatear(self):
        self.chocolate = True
    def has_choco(self):
        if self.chocolate:
            print("la galleta tiene chocolate")
        else:
            print("La galleta no tiene chocolate")

galleta = Galleta()
galleta.sabor="salado"
galleta.color="marron"
print("galleta color {}".format(galleta.color))
galleta.has_choco()
# print("galleta chocolate? {}".format(galleta.chocolate))
galleta.chocolatear()
galleta.has_choco()
# print("galleta chocolate? {}".format(galleta.chocolate))

class Pelicula():
    #constructor
    def __init__(self,titulo, duracion, lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print ("Se ha creado pelicula {}".format(self.titulo))
    #destructor
    def __del__(self):
        print ("Se ha borrado pelicula {}".format(self.titulo))
    #redefinicion de un metodo especial
    def __str__(self):
        return "{} Lanzada en {} con una duracion de {}".format(self.titulo,self.lanzamiento,self.duracion)

class Catalogo():
    peliculas=[]
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    def agregar_peliculas(self,p):
        self.peliculas.append(p)
    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print ("{} 00".format(pelicula))

p= Pelicula("el padrino",175,"diciembre 1972")
c = Catalogo([p])
c.mostrar_peliculas()
# del(p)
class Ejemplo_privado():
    __atributo_privado="soy un atributo inalcanzable"
    def __metodo_privado(self):
        print("te muestro mi atributo privado {}".format(self.__atributo_privado))
    def metodo_publico(self):
        self.__metodo_privado()

e=Ejemplo_privado()
# e.__atributo_privado
# e.__metodo_privado()
e.metodo_publico()

