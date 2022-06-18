
class ViajeUsuario():
    def __init__(self,dni,destino,cant_Dias):
        self.__dni = dni
        self.destino = destino
        self.cant_Dias = cant_Dias

    def VerDatos(self):
        print("DNI: ",self.__dni)
        print("Destino: ",self.destino)
        print("Cantidad de Dias: ",self.cant_Dias)

    def __DuracionEstadia(self):
        if self.cant_Dias > 7:
            return "Larga"
        else:
            return "Corta"

    def CalcularCostoPorDia(self):

        if self.destino == "Argentina": costoPorDia = 2000
        elif self.destino == "Brasil":  costoPorDia = 5000
        else:                           costoPorDia = 10000

        if (self.__DuracionEstadia == "Larga"): 
            costoPorDia -= costoPorDia/10           #10% menos

        return costoPorDia


def IngresarDNI():
    try: dni = int(input("Ingrese DNI: "))
    except ValueError:
        dni = 0

    while dni <= 0:
        print("!! Error !! Ingrese un DNI valido")

        try: dni = int(input("Ingrese DNI: "))
        except ValueError:
            dni = 0
    
    return dni

def IngresarDestino():
    destino = str(input("Ingrese Destino: "))

    while destino == "":
        print("!! ERROR !!. Por Favor ingrese un Destino")
        destino = str(input("Ingrese Destino: "))

    return destino

def IngresarCantDias():
    try: cantDias = int(input("Ingrese la Cantidad de Dias: "))
    except ValueError:
        cantDias = 0

    while cantDias <= 0:
        print("!! Error !! Ingrese un valor valido")

        try: cantDias = int(input("Ingrese la Cantidad de Dias: "))
        except ValueError:
            cantDias = 0

    return cantDias


def IngresarViajeUsuario():
        
    dni = IngresarDNI()

    destino = IngresarDestino()

    cant_Dias = IngresarCantDias()

    return ViajeUsuario(dni,destino,cant_Dias)


def PreguntarSiReingresarDestino():
    respuesta = str(input("Desea Reingresar el Destino? (Y/N): "))
    respuesta = respuesta.upper()

    while respuesta != "Y" and respuesta != "N":
        print("!! ERROR !! Ingrese unicamete Y o N ")
        
        respuesta = str(input("Desea Reingresar el Destino? (Y/N): "))
        respuesta = respuesta.upper()

    if respuesta == "Y": return True
    else:                return False

def PreguntarSiReingresarCantDias():
    respuesta = str(input("Desea Reingresar el la Cantidad de Dias? (Y/N): "))
    respuesta = respuesta.upper()

    while respuesta != "Y" and respuesta != "N":
        print("!! ERROR !! Ingrese unicamete Y o N ")
        
        respuesta = str(input("Desea Reingresar la Cantidad de Dias? (Y/N): "))
        respuesta = respuesta.upper()

    if respuesta == "Y": return True
    else:                return False




# MENU:

viaje_Usuario = IngresarViajeUsuario()
viaje_Usuario.VerDatos()

respuesta = PreguntarSiReingresarDestino()
if respuesta == True: 
    viaje_Usuario.destino = IngresarDestino()

respuesta = PreguntarSiReingresarCantDias()
if respuesta == True: 
    viaje_Usuario.cant_Dias = IngresarCantDias()

