
bloques = ["Lego","Rasti"]

juegos = ["Ajedres","Damas","TEG"]

muniecos = ["Playmovil","Barbie"]

def __SeleccionarCategoria():
    categoria = ""
    while (categoria != "bloques" and categoria != "juegos" and categoria != "muniecos"):
        categoria = input("Ingrese la Categoria deseada (Bloques/ Juegos/ Muniecos):")
        categoria = categoria.lower()
        if categoria == "":
            print("!! ERROR !! Ingrese una Categoria")
        elif (categoria != "bloques" and categoria != "juegos" and categoria != "muniecos"):
            print("!! ERROR !! Categoria Ingresada Incorrecta")

    if categoria == "bloques": return bloques
    elif categoria == "juegos": return juegos
    else: return muniecos

def VerCategoria():
    print(" --- Ver Categoria ---")
    categoriaSeleccionada = __SeleccionarCategoria()
    for juguete in categoriaSeleccionada:
        print("- ", juguete)

def IngresarJuguete():
    print(" --- Ingresar Juguete ---")
    categoriaSeleccionada = __SeleccionarCategoria()
    juguete = input("Ingrese el juguete que desea añadir: ")
    categoriaSeleccionada.append(juguete)

