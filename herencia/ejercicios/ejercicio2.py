class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )
class Auto(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return "Auto "+super().__str__()+" de {} y cilindrada de {} rpm".format(self.velocidad,self.cilindrada)
class Camioneta(Auto):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga=carga
    def __str__(self):
        return super().__str__()+" con capacidad de {} kg".format(self.carga)
class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        tipos=["urbana","deportiva"]
        if tipo not in tipos:
            print("tipo no valido")   
        self.tipo=tipo
    def __str__(self):
        return super().__str__()+" de tipo {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__()+" de velocidad {} y cilindrada de {} rpm".format(self.velocidad,self.cilindrada)




auto = Auto("rojo","aro 20","100kmh",1200)
camioneta = Camioneta("rojo","aro 20","100km/h",1200,"100")
bicicleta = Bicicleta("rojo","aro 20","urbana")
motocicleta = Motocicleta("rojo","aro 20","urbana","250km/h",1332)

print(auto)
print(camioneta)
print(bicicleta)
print(motocicleta)
vehiculos =[]
vehiculos.append(auto)
vehiculos.append(camioneta)
vehiculos.append(bicicleta)
vehiculos.append(motocicleta)
print (vehiculos)
