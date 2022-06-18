decorador="------------------"
vehiculos = []

class Vehiculo_Obj():
    def __init__(self,codigo,marca,modelo):
        self.codigo=codigo
        self.marca=marca
        self.modelo=modelo
        self.cant_Ruedas=4

    def ver(self):
        print(f"Vehiculo:\n-Codigo de Referencia: {self.codigo}\n-Marca: {self.marca}\n-Modelo: {self.modelo}\n-Cantidad de ruedas: {self.cant_Ruedas}")


def crear_Vehiculo():
    # Verifica que el codigo que se ingrese no lo este usando otro.
    while True:
        codigo_Vehiculo = int(input("Ingrese codigo de referencia: "))
        for i in vehiculos:
            if codigo_Vehiculo == i.codigo:
                print("Ya existe un vehiculo con ese codigo. Vuelva a Intentar")
                break
        else:
            break

    vehiculo = Vehiculo_Obj(
        codigo_Vehiculo,
        input("Ingrese marca: "),
        input("Ingrese modelo: ")
    )
    vehiculos.append(vehiculo)

def ver_Vehiculo():
    print(decorador)
    cod= int(input("Ingrese el codigo del vehiculo que desea buscar: "))

    for i in vehiculos:
        if i.codigo == cod:
            i.ver()
            break
    else:
        print("\nEl codigo ingresado no corresponde a ningun vehiculo")
            

    input("Presione ENTER para continuar") 


while True:
    print(decorador)
    opc= input("Indique la accion que desea realizar:\nA) Crear Vehiculo\nB) Ver Vehiculo\nC) Finalizar Programa\n> ")
    opc = opc.upper()

    if opc=="A":
        crear_Vehiculo()
    elif (opc=="B"):
        ver_Vehiculo()
    elif (opc=="C"):
        break
    else:
        input("Incorrecto. Vuelva a Intentar")
    