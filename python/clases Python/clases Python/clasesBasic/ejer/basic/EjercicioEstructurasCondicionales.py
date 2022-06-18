print("//////////////////// Inicio del Programa /////////////////////")

#1
print("AUTOMOTORES LA CARRETA - SISTEMA DE BÚSQUEDA DE VEHÍCULOS")

#2
monto_aGastar = int(input("Ingrese el monto que desea gastar: "))
#2.1
if (monto_aGastar < 500000):
    print("No se poseen vehículos de ese valor.")
    monto_aGastar = int(input("Ingrese el monto que desea gastar: "))

#3
marcaDeseada = input("Ingrese la marca del auto que esta buscando: ").upper() #pasa todo lo que esta en la string a MAYUSCULA
#3.1
if (marcaDeseada != "FORD" and marcaDeseada != "CHEVROLET"):
    print("Solo se podeen autos de marca Ford y Chevrolet")
    marcaDeseada = input("Ingrese la marca del auto que esta buscando: ").upper()

#4
cantidadPuertasDeseadas = int(input("Indique la cantidad de puertas deseadas: "))
#4.1
if(cantidadPuertasDeseadas < 3 or cantidadPuertasDeseadas > 5):
    print("Unicamente se poseen autos de 3,4 o 5 puertas")
    cantidadPuertasDeseadas = int(input("Indique la cantidad de puertas deseadas: "))


if(marcaDeseada == "CHEVROLET"):

    if(monto_aGastar < 800000):
        print("No hay CHEVROLET a ese precio")
    
    elif(3 <= cantidadPuertasDeseadas <= 5):
        print("> CHEVROLET AVEO")

    else:
        print("No se poseen vehículos con esos requerimientos.")

elif(marcaDeseada == "FORD"):

    if (cantidadPuertasDeseadas == 3 and monto_aGastar < 700000):
        print(">FORD KA")

    else:
        print("No se poseen vehículos con esos requerimientos.")

else:
    print("No se poseen vehículos con esos requerimientos.")


print("//////////////////// Fin del Programa /////////////////////")