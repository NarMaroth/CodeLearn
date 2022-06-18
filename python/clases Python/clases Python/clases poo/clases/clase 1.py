class Platos():

    material="Ceramica"
    color="Blanco"
    diametro=20
    alto=10
    precio=220

    def calcular_Vol(self):
        self.vol= self.diametro* self.alto
        print("El volumen es", self.vol)

#Creaun un obj      ---     Instancia de una clase:

plato1 = Platos()
print(plato1.color)

plato2 = Platos()
plato2.precio = 330
print(plato2.precio)

#LLamar funciones de un obj.

plato1.calcular_Vol()