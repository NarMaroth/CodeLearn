

#       Funciones:
def compraElectrodomestico():
    electroDeseado = input("Indique qué electro desea comprar:\n a) Lavarropas $30000\n b) Heladera $50000\n c) Licuadora $3000\n > ")
    
    if (electroDeseado == "a"):
        costo = 30000
    elif (electroDeseado == "b"):
        costo = 50000
    else:
        costo = 3000

    return costo

def compraMusica():
    musicaDeseada = input("Indique qué musica desea comprar:\n a) Beatles $300\n b) Queen $350\n c) Soda $325\n > ")
    
    if (musicaDeseada == "a"):
        costo = 300
    elif (musicaDeseada == "b"):
        costo = 350
    else:
        costo = 325

    return costo

#       Main:

print("//////////////////// Inicio del Programa /////////////////////")

print("Bienvenido a Musimundo")

opcion = input("Seleccione por teclado algunas de las siguientes opciones:\n a) Comprar electrodomésticos\n b) Comprar música\n c) Comprar ambos\n > ")

if (opcion == "a"):
    costoTotal = compraElectrodomestico()

elif(opcion == "b"):
    costoTotal = compraMusica()

else:
    costoTotal = compraElectrodomestico() + compraMusica()

print("Costo final de su compra: " + str(costoTotal))

print("Gracias por su compra")

print("//////////////////// Fin del Programa /////////////////////")