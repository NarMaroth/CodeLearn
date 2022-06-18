
# ENCAPSULAMIENTO

# Encapsular un atributo hace que este no pueda ser modificado desde fuera de la clase

class ALUMNO():
    def __init__(self,nombre):
        self.nombre = nombre
        self.__nacionalidad = "Argentino"    #Se encapsula añadiendo 2 barras bajas al principio del atributo

    def informar(self):
        self.__nacionalidad = "Chino"
        print(self.nombre , "es" , self.__nacionalidad)

    def __test(self): # Un metodo encapsulado solo podra ser llamado desde dentro de la clase
        print("Hola")


a1 = ALUMNO("pepe")

# Al intentar modificar el atributo __nacionalidad desde fuera de la clase no pasa nada
a1.__nacionalidad = "Brasilero"
a1.informar()

# Si se intenta llamar un metodo encapsulado desde fuera de la clase dara error.
a1.__test()