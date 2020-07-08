class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )
def Auto(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(color,ruedas)
        self.velocidad
        self.cilindrada
