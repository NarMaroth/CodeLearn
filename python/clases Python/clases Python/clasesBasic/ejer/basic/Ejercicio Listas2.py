
libros = ["La Sirenita", "Blancanieves", "Cenicienta"]

def verLibros():
    print("     Libros disponibles:")

    print(libros)

    continuar = input("ENTER para continuar:") # Es para poder leer el texto abajo del todo y que no salte automaticamenta para arriba
    print("---------------------------------------------")       

def anadirLibro():
    print("     Añadir Libro:")

    nuevoLibro = input("- Ingrese el nombre del nuevo libro:")

    if (nuevoLibro in libros):
        print("-- El Libro ya se encuentra en la biblioteca.")
    else:
        libros.insert(0,nuevoLibro)

    continuar = input("- Desea Continuar?: (Y/N) ")
    continuar = continuar.upper()
    if (continuar == "Y"):
        anadirLibro()

    print("---------------------------------------------")
    
def eliminarLibro():
    if (len(libros) > 0):
        print("     Eliminar Libro:") 

        print(libros)
        libro_a_Eliminar = input("- Ingrese el nombre del libro que desea Eliminar: ")

        if (libro_a_Eliminar not in libros):
            print("-- Libro ingresado no se encuentra en la biblioteca.")
        else:
            libros.pop( libros.index(libro_a_Eliminar) )

        continuar = input("- Desea Continuar?: (Y/N) ")
        continuar = continuar.upper()
        if (continuar == "Y"):
            eliminarLibro()
        else:
            print("---------------------------------------------")
    else:
        print("-- No quedan mas libros para eliminar")
        continuar = input("ENTER para continuar:")
        print("---------------------------------------------")

def verStock():
    print("     Stock del Libros:")
    print("- La Biblioteca dispone de una cantidad de",len(libros), "libros")

    continuar = input("ENTER para continuar:")
    print("---------------------------------------------")

    return

def opciones():
    print("Indique la accion que desea ralizar:")
    opcionElegida = input(print("A) Ver los libros disponibles \nB) Agregar Libro \nC) Eliminar libro \nD) Ver Stock \nE) Salir"))
    opcionElegida = opcionElegida.upper()

    if (opcionElegida == "A"):
        verLibros()
    elif (opcionElegida == "B"):
        anadirLibro()
    elif (opcionElegida == "C"):
        eliminarLibro()
    elif (opcionElegida == "D"):
        verStock()
    elif (opcionElegida != "E"):
        print(" !!! Respuesta Incorrecta ¡¡¡ Vuelva a Intentar")
    else:
        print("---------------Fin del Programa----------------------")
        return

    opciones()


print("Biblioteca Nacional")

opciones()

