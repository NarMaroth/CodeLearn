decorador = "-"*20

class PERSONAS():
    def __init__(self):
        self.nombre =   input("Ingresa nombre: ")
        self.dni =      int(input("Ingrese el dni: "))

    def ver_Datos(self):
        print(decorador)
        print(f"DATOS PERSONALES\nNombre: {self.nombre}\nDNI: {self.dni}")
        print(decorador)


class CLIENTES(PERSONAS):
    pass

class EMPLEADO(PERSONAS):
    def calcular_Sueldo(self):
        self.sueldo = int(input("Ingrese sueldo:"))
        self.antiguedad = int(input("Ingrese antiguedad: "))
        self.sueldo_Final = self.sueldo + (self.sueldo* (self.antiguedad*0.1))
        print(f"Su sueldo final es {self.sueldo_Final}")

class REPOSITOR(EMPLEADO):
    pass

cliente_1 = CLIENTES()
cliente_1.ver_Datos()


empleado_1 = REPOSITOR()
empleado_1.ver_Datos()
empleado_1.calcular_Sueldo()