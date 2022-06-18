from gestion.usuarios.login import valdiarContraseña,esEncargado
from gestion.productos.stock import VerCategoria,IngresarJuguete


def IngresarNombre():
    nombre = ""
    while (nombre == ""):
        nombre = input("Ingrese su nombre: ")
        if (nombre == ""): print ("!! ERROR !!")

    return nombre

def IngresarCargo():
    cargo = ""
    while (cargo == "") :
        cargo = input("Ingrese su cargo: ")
        cargo = cargo.lower()
        if (cargo == ""): print("!! ERROR !! ")

    return cargo

def IngresarContraseña():
    contraseña = ""
    while (contraseña == ""):
        contraseña = input("Ingrese su contraseña: ")
        if (contraseña == ""): print("!! ERROR !! ")

    return contraseña

def IngresarEleccion():
    eleccion = 0
    while (eleccion != 1 and eleccion != 2 and eleccion != 3):
        try:
            eleccion = int(input("-> "))
        except ValueError:
            print("")       # Para que el programa continue

        if (eleccion != 1 and eleccion != 2 and eleccion != 3): 
            print("!! ERROR !! Ingrese unicamente 1,2 o 3")

    return eleccion

def Menu():
    eleccion = 0
    while (eleccion != 3):
        print("\n --- Menu ---")
        print ("1) Ver Categoria.")
        print ("2) Añadir juguete a catagoria.")
        print ("3) Salir del Menu.")

        eleccion = IngresarEleccion()
        if eleccion == 1: VerCategoria()
        elif eleccion == 2: IngresarJuguete()


print("\n        --------  Jugueteria el Tren Loco  ---------\n")

nombre_Usuario = IngresarNombre()
cargo_Usuario = IngresarCargo()

    #Validar Usuario
if (esEncargado(cargo_Usuario) == False): 
    print("\n!! Solo los Encargados Pueden Acceder al Sistema !!")

else:
    # Validar Contraseña 
    contraseña_Usuario = ""
    while (valdiarContraseña(contraseña_Usuario) == False):
        contraseña_Usuario = IngresarContraseña()
        if (valdiarContraseña(contraseña_Usuario) == False): 
            print("!! ERROR !! Contraseña Incorrecta")

    # Ingresar Menu
    Menu()

print ("      --------  Programa Finalizado  ---------\n")