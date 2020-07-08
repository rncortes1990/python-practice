import math

class Punto():
    x = 0
    y = 0
    def __init__(self,coordX=0,coordY=0):
        self.x = coordX
        self.y = coordY
        print("Se ha creado el punto de coordenada X:{},Y:{}".format(self.x,self.y))
    def __str__(self):
       return ("El punto tiene coordenada {coordX},{coordY}".format(coordX=self.x,coordY=self.y))

    def cuadrante(self):
        cuadrante = None

        if self.x>0 and self.y>0:
            cuadrante = "I"
        elif self.x>0 and self.y<0:
            cuadrante = "IV"
        elif self.x<0 and self.y>0:
            cuadrante = "II"
        elif self.x<0 and self.y<0:
            cuadrante = "III"
        elif self.x==0 and self.y!=0:
            print("El  punto ({},{}) está en el eje Y".format(self.x,self.y)) 
            return
        elif self.y==0 and self.x!=0:
            print("El  punto ({},{}) está en el eje X".format(self.x,self.y)) 
            return
        else:
            print("El  punto esta en el origen O ({},{})".format(self.x,self.y))  
            return 
        print("el punto ({},{}) pertenece al cuadrante {}".format(self.x,self.y,cuadrante))
    def vector(self,punto):
        x = punto.x - self.x
        y = punto.y - self.y
        return x,y
    def modulo(self,punto):
        calculo = (punto.x - self.x)**2 + (punto.y - self.y)**2 
        modulo = math.sqrt(calculo)
        return modulo

class Rectangulo:
    def __init__(self,puntoInicial=Punto(),puntoFinal=Punto()):
        self.puntoInicial = puntoInicial
        self.puntoFinal = puntoFinal
        self.base = abs(puntoFinal.x -self.puntoInicial.x)
        self.altura = abs(puntoFinal.y -self.puntoInicial.y)
        self.area = self.base * self.altura

    def showBase(self):
        print("La base del rectangulo es {}".format(self.base))
    def showAltura(self):
        print("La altura del rectangulo es {}".format(self.altura))
    def showArea(self):
        print("El area del rectangulo es {}".format(self.area))


def masLejano(*args):
        origin=Punto()
        isHigher=0
        puntoMayor=None
        for arg in args:
            ifisHigher == 0:
                aux=origin.modulo(arg)
                isHigher = 1
                puntoMayor = arg
            else:
                module=origin.modulo(arg)
                if aux<module:
                    aux=module
                    puntoMayor = arg
        print("el punto mas lejano es{},{}".format(puntoMayor.x,puntoMayor.y))





p1 = Punto(2,3)
p2 = Punto(5,5)
p3 = Punto(-3,-1)
p4 = Punto(0,0)
p5 = Punto(0,-10)
p6 = Punto(20,0)
p1.cuadrante()
p2.cuadrante()
p3.cuadrante()
p4.cuadrante()
p5.cuadrante()
p6.cuadrante()
print (p6.vector(p5))
print (p6.modulo(p5))
r = Rectangulo(p1,p2)
r.showBase()
r.showAltura()
r.showArea()
masLejano(p6,p6)
