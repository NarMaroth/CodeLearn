
# Metodo Constructor

# Siempre es lo 1ero de la clase    

class Alumnos():
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
        self.nacionalidad="Argentina"

    def ver(self):
        print(f"El alumno es {self.nombre} su dni es {self.dni} y es de {self.nacionalidad}")


alumno1= Alumnos("Jose",11012001)

alumno1.ver()

print(alumno1.nombre)

alumno2 = Alumnos(
    input("Ingrese su nombre: "),
    int(input("Ingrese su dni: "))
)

alumno2.ver()