
class PELICULA():
    def __init__(self,titulo,añoEstreno):
        self.titulo = titulo
        self.añoEstreno = añoEstreno

    def VerInforme(self):
        print(f"Titulo: {self.titulo}\n- Estreno: {self.añoEstreno}")


class NACIONAL(PELICULA):
    def __init__ (self,titulo,añoEstreno,protagonista):
        super().__init__(titulo,añoEstreno)

        self.protagonista = protagonista

    def VerInforme(self):
        print(f"Titulo: {self.titulo}\n- Protagonista: {self.protagonista}\n- Estreno: {self.añoEstreno}")


class ACCION(PELICULA):
    def __init__(self,titulo,añoEstreno,paisOrigen):
        super().__init__(titulo,añoEstreno)

        self.paisOrigen = paisOrigen
    
    def VerInforme(self):
        print(f"Titulo: {self.titulo}\n- Estreno: {self.añoEstreno}\n- Pais de Origen: {self.paisOrigen}")


class TERROR(PELICULA):
    def __init__(self,titulo,añoEstreno,clasificacion):
        super().__init__(titulo,añoEstreno)

        self.clasificacion = clasificacion

    def CalificadaParaMayores(self):
        if (self.clasificacion == "G" or "PG" or "PG-13"):
            return False
        else:
            return True

def IngresarRespuesta():
    respuesta = 0
    while respuesta != 1 and respuesta != 2 and respuesta != 3 and respuesta != 4:
        try:
            respuesta = int(input("->"))
        except ValueError:
            print("")
        if respuesta != 1 and respuesta != 2 and respuesta != 3 and respuesta != 4:
            print("!! ERROR !! Ingrese unicamente 1,2,3 o 4")

    return respuesta

class TERROR_NACIONAL(NACIONAL, TERROR):
    def __init__(self,titulo,añoEstreno,protagonista,clasificacion):
        NACIONAL.__init__(self,titulo,añoEstreno,protagonista)
        TERROR.__init__(self,titulo,añoEstreno,clasificacion) 

    def SalasDisponibles(self):
        print(" Indique de que Zona desea ver las salas disponibles:")
        print("1) Zona Norte")
        print("2) Zona Sur")
        print("3) Zona Este")
        print("4) Zona Oeste")
        respuesta = IngresarRespuesta()
        if respuesta == 1: print(" Las salas disponibles en Zona Norte son: 3")
        elif respuesta == 2: print(" Las salas disponibles en Zona Sur son: 7")
        elif respuesta == 3: print(" Las salas disponibles en Zona Este son: 2")
        else: print(" Las salas disponibles en Zona Oeste son: 6")

terrorNacional1 = TERROR_NACIONAL("1","2","3","G")