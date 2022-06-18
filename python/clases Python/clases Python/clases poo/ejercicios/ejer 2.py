decorador="------------------"

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.cant_Ruedas=4

    def ver(self):
        print(decorador)
        print(f" Vehiculo Creado:\n-Marca: {self.marca}\n-Modelo: {self.modelo}\n-Cantidad de ruedas: {self.cant_Ruedas}")
        print(decorador)


vehiculo1 = Vehiculo(
    input("Ingrese la marca deseada para el vehiculo: "),
    input("Ingrese el modelo deseado: ")
)

vehiculo1.ver()